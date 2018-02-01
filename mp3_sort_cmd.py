import shutil,os,time,lyrics
from colorama import init, Fore
init() # filter ANSI escape sequences out of any text sent to stdout or stderr, and replace them with equivalent Win32 calls

curdir = os.getcwd()
# folderPath = os.path.dirname(os.getcwd())

#nameRegex = re.compile(r'(?P<name>.*)\.(?P<ext>mp3)')

songTypeDict = {'other':0,'o':0,'soundtrack':1,'s':1,'lyric':2,'l':2,'classic':3,'c':3}
typeToFolder = {0:'other', 1:'Soundtrack', 2:'Lyric', 3:'Classic'}

def fileNameTest(filename):
    return ('mp3_sort' not in filename) and ('ini' not in filename) and ('.project' not in filename) and ('.pydevproject' not in filename) and ('py' not in filename) and (os.path.isfile(filename) and ('.m3u' not in filename) and ('.txt' not in filename) and ('.html' not in filename))

def userInput():
    type_input = input()
    songType = songTypeDict.setdefault(type_input.lower(),0)
    return songType
    
def songInput():
    appendToPlaylist = input('Append File To Playlist?(Y/N)')
    appendToPlaylist = 'y' in appendToPlaylist.lower()
    for filename in os.listdir(curdir):
        if (fileNameTest(filename)):
            print(Fore.GREEN + '\t' + filename)
            print(Fore.BLACK)
            songType = userInput()
            songFolder = typeToFolder[songType]
            
            if songFolder == 'other' :
                print(Fore.WHITE + '\t\t>>>' + Fore.MAGENTA + songFolder)
                break
        
            if appendToPlaylist:
                print(Fore.WHITE + '\t\t>>>' + Fore.CYAN + songFolder)
                with open(os.path.join(curdir,'a.m3u'),"a") as file:
                    file.write('\n' + songFolder + '/' + filename)
                
            os.makedirs(os.path.join(curdir,songFolder), exist_ok=True)
            shutil.move(os.path.join(curdir,filename),os.path.join(curdir,songFolder,filename))
            if songType == 2: #For Lyrics
                lyrics.addLyric()
                


if __name__ == '__main__':
    print('\n\n\n\nInput: C/Classic, L/Lyric, S/Soundtrack, O/Other, J')
    print('Song Type for:')
    songInput()

    
    
    time.sleep(3)
    
    #deinit() #If init() from colorama is used, deinit() will disable.
