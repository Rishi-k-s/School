import csv


file_handlr = open("D:\Dev\python\Testing_School\File Operations (CH2)\gucci.csv","r",newline="\n")

wrriter_obj = csv.reader(file_handlr)
print(file_handlr.seek(30))
for i in wrriter_obj:
    print(i)
print(file_handlr.tell())
file_handlr.close()
    

