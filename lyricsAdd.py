import os
#import xlrd
#import xlsxwriter as xlw

#workbook = xlw.Workbook('C://Users//Blue2015//Google Drive//Synced//MP3//Lyrics.xlsx')
#worksheet = workbook.add_worksheet()

#o_workbook = xlrd.open_workbook('C://Users//Blue2015//Google Drive//Synced//MP3//Lyrics.xlsx')
#o_sheet = o_workbook.sheet_by_index(0)
#rows = o_sheet.nrows

pardir = os.path.dirname(os.getcwd())

##Takes Input On Song Name And URL To Lyrics
print('Name: ')
songName = input()
print('URL: ')
link = input()

#worksheet.write(rows+1,0,songName)
#worksheet.write(rows+1,1,link)
#workbook.close()

#import xlutils.copy as copy

#workbook = copy.copy(o_workbook)
#sheet = workbook.get_sheet(0)
#sheet.write(rows + 1 , 0 , songName)
#sheet.write(rows + 1 , 1 ,link)
#workbook.save('C://Users//Blue2015//Google Drive//Synced//MP3//Lyrics.xlsx')

##Opens A Text File Containing *url* | *name* for each song
with open (os.path.join(pardir,'lyrics.txt'),'a') as file:
    file.write('\n' + link + ' | ' + songName)##Adds New Input


exec(open(os.path.join(pardir,'createSort.py')).read())##Copies Song/URLs from text file to lyricsSortedInput.txt
exec(open(os.path.join(pardir,'sortTxt.py')).read())##Takes Input from above and outputs sorted version to lyricsSortedOutput.txt
exec(open(os.path.join(pardir,'xlCreate.py')).read())##Puts Sorted Output and writes to excel spreadsheet 
exec(open(os.path.join(pardir,'lyricsUpdateHTML.py')).read())##Reads Excel sheet to create HTML page of links

print('lyricsAdd')


time.sleep(3)
