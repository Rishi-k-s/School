file_handlr = open("D:\School\File Operations (CH2)\school_Dat.txt","r")
line_list = file_handlr.readlines()
for each_line in line_list:
    seperateEachWords = each_line.split()
    for each_word in seperateEachWords:
        print('{} # '.format(each_word), end='')
file_handlr.close()