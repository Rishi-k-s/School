# Write a program in python using function to print all the prime numbers within a range
# (including upper and lower limit).


def primeNos():
    getRangeFront = int(input("Enter First number : "))
    getRangeLast =  int(input("Enter second number: "))
    for getNum in range(getRangeFront,getRangeLast+1):
        isPrime = True
        for eachDigit in range(2,int(getNum)//2+1):
            if (getNum % eachDigit == 0):
                isPrime = False
                break
        if (isPrime == True):
            print("{} is prime".format(getNum))

# Write a python program to read an integer number from the user and to find the sum of
# digits and reverse of a number using function.
# getNum = int(input("Enter a number: "))
# revNum = 0
# sum1 = 0
# while getNum > 0:
#     lastNum = getNum%10
#     sum1 = sum1 + lastNum
#     revNum = lastNum + revNum * 10
#     getNum = getNum // 10
# print(revNum,sum1)

#impliment stack using list

# def pushOn(book):         
#     mainStack.append(book)
# def Pop():
#     if(bool(mainStack) == False):
#             print("There is no element to remove")
#     else:
#         print("{} is removed".format(mainStack.pop()))
# mainStack = []

# while True:
#     print("[1] Add book \n[2]Remove book")
#     getSelection = int(input("-->"))
#     if(getSelection == 1):
#         book = input("Enter book to add: ")
#         pushOn(book)
#     elif(getSelection == 2):
#         Pop()


# getNum = int(input("Enter a number: "))
# sum1 = 0
# reverse = 0
# while getNum > 0:
#     lastDig = getNum%10
#     reverse = lastDig + reverse * 10
#     sum1 = sum1 + lastDig
#     getNum //= 10
# print("sum: ",sum1)
# print("rev:" , reverse)

# uppNum = int(input("Enter upper limit: "))
# lowNum = int(input("Enter lower limit: "))
# for p in range (uppNum,lowNum+1):
#     isPrime = True
#     for i in range (2,p//2+1):
#         if(p%i == 0):
#             isPrime = False
#             break
#     if(isPrime):
#         print(p,"is prime")
#     else:
#         print(p,"is not prime")

# CREATE TABLE product (
#     PCode varchar(255),
#     Pname varchar (255),
#     Weight int,
#     Price int,
#     Qty int,
# );

# SELECT * FROm employees


# import pickle

# file_handlr_w = open("numbers.dat","wb")

# getTimes = int(input("Enter number of times: "))
# mainList = []
# for i in range(getTimes):
#     getNum = int(input("Enter number: "))
#     mainList.append(getNum)
# pickle.dump(mainList,file_handlr_w)
# file_handlr_w.close()

# file_handlr_r = open("numbers.dat","rb")
# lines  = pickle.load(file_handlr_r)
# print(lines)
# for eachList in lines:
#     print(eachList)



import csv

# file_handlr_w = open("one.csv","w",newline= "\n")
# header = ["Roll No","Name","Marks"]
# csvWriter = csv.writer(file_handlr_w)
# csvWriter.writerow(header)
# mainList = []
# getTimes = int(input("Enter the number of times: "))

# for i in range(getTimes):
#     getRool = int(input("ENter roll: "))
#     getName = input("Enter name: ")
#     getMarks = int(input("Enetr mrks: "))
#     userList = [getRool,getName,getMarks]
#     mainList.append(userList)
# csvWriter.writerows(mainList)
# file_handlr_w.close()
# file_handlr_w = open("one.csv","r")
# csvReader = csv.reader(file_handlr_w)
# for i in csvReader:
#     for p in i:
#         print(p,end="\t")
#     print()

l1 = [1,2,3,4,5]

print(l1[:])
