file_handlr = open("D:\School\File Operations (CH2)\school_Dat.txt","r")
line_list = file_handlr.readlines()
vovels = 'aeiouAEIOU'
vovCounter,upperCount,lowerCount,consonantCount = 0,0,0,0
for each_line in line_list:
    for each_letter in each_line:
        if each_letter in vovels:
            vovCounter+=1
        if each_letter not in vovels:
            consonantCount+=1
        if each_letter.isupper():
            upperCount +=1
        elif each_letter.islower():
            lowerCount +=1
print('No. of vovels{}\nNo. of consonants{}\nNo. of Uppercase{}\nNO. of lowercase{}'.format(vovCounter,consonantCount,upperCount,lowerCount))