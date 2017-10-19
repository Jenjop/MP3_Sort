import re,os

pardir = os.path.dirname(os.getcwd())

lyricsRegex = re.compile(r'''
    (http.*)    #Link --> Group 1
    \s\|\s      #Seperator
    (.*)     #Extension --> Group 2
    ''',re.VERBOSE)

with open (os.path.join(pardir,'lyrics.txt')) as file:
    lyrics = file.read()

#print(lyrics)

with open (os.path.join(pardir,'lyricsSortedInput.txt'),'r+') as file:
    file.truncate(0)
    #file.seek(0)
    for line in lyricsRegex.finditer(lyrics):
        #print(line)
        link = line.group(1)
        name = line.group(2)
        #print()
        file.write(link + ' | ' + name + '\n')
        #print(name)

print('createSort')
