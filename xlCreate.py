import re,os
import xlsxwriter as xlw

pardir = os.path.dirname(os.getcwd())

workbook = xlw.Workbook(os.path.join(pardir,'Lyrics.xlsx'))
worksheet = workbook.add_worksheet()
row = 0

lyricsRegex = re.compile(r'''
    (http.*)    #Link --> Group 1
    .*\|      #Seperator
    (.*)     #Extension --> Group 2
    ''',re.VERBOSE) ##Use re.VERBOSE to allow with ''' to allow regex to span multiple lines
#lyricsRegex2 = re.split(r'\n')

with open (os.path.join(pardir,'lyricsSortedOutput.txt')) as file:
	lyrics = file.read()
#print(lyrics)
#search = lyricsRegex.search(lyrics)
    
#links = search.group(1)
#print('Links: ' + links)

#names = search.group(2)
#print('names: ' + names)

#print(search)

for line in lyricsRegex.finditer(lyrics):
    link = line.group(1)
    name = line.group(2)
    worksheet.write(row,0,name)#song name
    worksheet.write(row,1,link)#link to lyrics
    row +=1
    #print(links2)
    #print(name)
    #print(line)

workbook.close()

print('xlCreate')
