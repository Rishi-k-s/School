import pickle

file_handlr = open("D:\Dev\python\Testing_School\File Operations (CH2)\oomidat.dat","rb")

try:
    for i in file_handlr:
        print(i)
        print(pickle.load(file_handlr))
except Exception as e:
    print(e)
# for each_line in line_list:
#     seperateEachWords = each_line.split()
#     for each_word in seperateEachWords:
#         print('{} # '.format(each_word), end='')
file_handlr.close()