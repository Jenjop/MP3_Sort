import re,shutil,os,time
from colorama import init, Fore
init() # filter ANSI escape sequences out of any text sent to stdout or stderr, and replace them with equivalent Win32 calls

filePath = os.getcwd()
#folderPath = os.path.dirname(os.getcwd())

nameRegex = re.compile(r'''
    (.*)    #Name of file --> Group 1
    \.      #Period
    mp3     #Extension
    ''',re.VERBOSE) ##Use re.VERBOSE to allow with ''' to allow regex to span multiple lines

def fileNameTest(filename):
        if ('mp3' in filename):
                if ('musicScript' not in filename):
                        if('desktop' not in filename):
                                if ('py' not in filename):
                                        if ('txt' not in filename):
                                            return True
                                        else:
                                            return False
                                else:
                                        return False
                        else:
                                return False
                else:
                        return False
        else:
                return False


print('\n\n\n')
##User Inputs Music Type When Given File Name
print('O/OST, C/Classic, L/Lyrics, U/cUstom, N/NotMusic, J')
print('Song Type for:')
for filename in os.listdir(filePath):
    if (fileNameTest(filename)):
        print(Fore.GREEN + '\t' + filename)
        print(Fore.BLACK)
        songType = input()
        if ('notmusic' in songType.lower() or 'n' in songType.lower()):
            songType = 'NotMusic'        
        elif ('ost' in songType.lower() or 'o' in songType.lower()):
            songType = 'OST'
        elif ('lyrics' in songType.lower() or 'l' in songType.lower()):
            songType = 'Lyrics'
        elif ('classic' in songType.lower() or 'c' in songType.lower()):
            songType = 'Classic'
        elif ('j' in songType.lower() or 'j' in songType.lower()):
            songType = 'J'
        elif ('custom' in songType.lower() or 'u' in songType.lower()):
            songType = 'custom'

        if songType != 'NotMusic' :
            nameSearch = nameRegex.search(filename)
            songName = nameSearch.group(1)
            print(Fore.WHITE + '\t\t>>>' + Fore.CYAN + songType)
            with open(os.path.join(filePath,'playlist.m3u'),"a+") as file:
                file.write('\n' + songType + '/' + filename)
            if not os.path.exists(os.path.join(filePath,songType)):
                os.makedirs(os.path.join(filePath,songType))    
            shutil.move(os.path.join(filePath,filename),os.path.join(filePath,songType,filename))
            if songType == 'Lyrics':
                exec(open(os.path.join(filePath,'lyricsAdd.py')).read())


        else:
            print(Fore.WHITE + '\t\t>>>' + Fore.MAGENTA + songType)

time.sleep(3)

#deinit() #If init() from colorama is used, deinit() will disable.
