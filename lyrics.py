import re,os

pardir = os.path.join(os.path.dirname(os.getcwd()),'mp3')

lyricsRe = re.compile(r'(?P<link>.*?)(?P<seperator>\s\|\s)(?P<name>.*)')

def sortNames():
    with open (os.path.join(pardir,'lyrics.txt'),'r+') as file:
        lyrics = file.read()
        lyrics_dict = {line.group('name'):line.group('link') for line in lyricsRe.finditer(lyrics)}
        file.truncate(0)
        for name in sorted(lyrics_dict.keys()):
            file.write(f'{lyrics_dict[name]} | {name}\n')
        file.close()
#         print('Sorted')
    return lyrics_dict
            
def createHTML(lyrics_dict: dict):
    beg = '<div>\n<a style=\"vertical-align: left; text-decoration: none;\" target=\"_blank\" href = \"'##Opening Tag for Link
    mid = '\">\n'##Closes <a> tag
    end = '</a>\n</div>\n'##Ends <a> tag
    
    with open(os.path.join(pardir,'lyrics.html'),'r+') as file:
        file.truncate(0)
        file.write('<html>\n<head>\n</head>\n<body>')##Beginning of HTML
        for name in sorted(lyrics_dict.keys()):
            file.write(f'{beg}{lyrics_dict[name]}{mid}{name}{end}')
        file.write('</body>\n</html>')
        file.close()     
    print('FileCreated')
    
def addLyric():
    songName = input('Name: \n')
    link = input('URL: \n')

    with open(os.path.join(pardir,'lyrics.txt'),'a') as file:
        file.write('\n' + link + ' | ' + songName)
        
    lyrics_dict = sortNames()
    createHTML(lyrics_dict)

# if __name__ == '__main__':
