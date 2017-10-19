import xlrd,time,os

pardir = os.path.dirname(os.getcwd())

workbook = xlrd.open_workbook(os.path.join(pardir,'Lyrics.xlsx'))
sheet = workbook.sheet_by_index(0)



#print (sheet.cell(0,1).value)
#print(sheet.nrows)
out = '<html>\n<head>\n</head>\n<body>'
beg = '<div>\n<a style=\"vertical-align: left; text-decoration: none;\" target=\"_blank\" href = \"'
mid = '\">\n'
end = '</a>\n</div>\n'
for i in range(sheet.nrows):
    out += beg + sheet.cell(i,1).value + mid + sheet.cell(i,0).value + end
    #print (beg + sheet.cell(i,1).value + mid + sheet.cell(i,0).value + end)
    #time.sleep(.01)
    
out +='</body>\n</html>'
#print(out)

with open (os.path.join(pardir,'lyrics.html'),'r+') as file:
    file.truncate(0)
    file.write(out)
    file.close()

print('lyricsUpdateHTML')
#print(out)
