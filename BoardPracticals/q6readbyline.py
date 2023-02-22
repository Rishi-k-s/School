file_handlr = open(r"D:\Dev\python\Testing_School\BoardPracticals\textfile.txt","r",newline="\n")
getLines = file_handlr.readlines()
LineWithA = []
vov,coson,upp,low = 0,0,0,0
vovels = "AEIOUaeiou"
for eachLine in getLines:
    wordList =eachLine.split()
    for eachWord in wordList:
        for eachLetter in wordList:
            if eachLetter in vovels:
                vov+=1
            else:
                coson+=1
            if(eachLetter.isupper()):
                upp+=1
            elif(eachLetter.islower()):
                low+=1        
print("vov: {}  consosnts: {}    upp: {}  low: {}".format(vov,coson,upp,low))




# import csv
# file_handlr = open(r"D:\Dev\python\Testing_School\BoardPracticals\one.csv","w")
# header = ["rollno","name","marks"]
# lines = []
# csvWriter = csv.writer()
# getTimes = int(input("Enter the no. of times:"))
# for i in range(getTimes):
# roll_no =
