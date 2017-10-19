#import pandas
#dataFrame = pandas.read_csv('C://Users//Blue2015//Google Drive//Synced//MP3//lyrics.txt',delimiter = '|', header = None)
#dataFrame.sort([0])
import re,os

pardir = os.path.dirname(os.getcwd())

lyricsRegex = re.compile(r'''
    (http.*)    #Link --> Group 1
    \s\|\s      #Seperator
    (.*)     #Extension --> Group 2
    ''',re.VERBOSE)

out = ''

with open(os.path.join(pardir,'lyricsSortedInput.txt'),'r+') as file:
    data = file.readlines()
    #print(data[1])
    #print(data[1].split("|")[1])
    data.sort(key=lambda x: x.split("|")[1])
    
    #file.truncate(0)
    #print(data[2])
    #file.seek(0)
    for line in data:
        search = lyricsRegex.search(line)

        name = search.group(2)
        link = search.group(1)
        out += link + ' | ' + name + '\n'
        #file.write(link + '| ' + name + '\n')
        #file.write('txt')

        #print(line)
        #file.write(line)
        
        #print(search)
        #print(name)
        #print(line)
    #print(out)
        
    #sorted = data.sort()
    #print(data)
    #print(data)
    #print(sorted)

with open(os.path.join(pardir,'lyricsSortedOutput.txt'),'r+') as file:
    file.truncate(0)
    file.write(out)
    
print('sortTxt')
