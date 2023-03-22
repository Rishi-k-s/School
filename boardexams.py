# def func1(a,b):
#     c = a+b 
#     print(c)

# x = 10
# y =20
# func1(x,y)

# def func1(*sidhan):
#     for i in sidhan:
#         print(i)


# func1(10,20,30)

# x = 6 < 12 and not (20 > 15) or (10 > 5) 
# print(x)

# def change(A):
#     S=0
#     for i in range(len(A)//2):
#         S += (A[i]*2)
#     return S
# B = [10,11,12,30,32,34,35,38,40,2]

# C = change(B)

# print('Output is',C) 


# def Sum3(L):
#     sum = 0
#     for i in L:
#         if(i%10 == 3):
#             sum+= i
#     return sum
# print(Sum3([ 123, 10, 13, 15, 23]))

# def ChangeGender():
#     changedList = []
#     fp_r = open("BIOPIC.txt","r")
#     lineList = fp_r.readlines()
#     for eachLine in lineList:
#         newLine = eachLine.replace("he","she")
#         changedList.append(change)

# ChangeGender()

# def ChangeGender():
#     fp_r = open("BIOPIC.txt","r")
#     line = fp_r.read()
#     newline = line.replace("he","she")
#     print(newline)

# ChangeGender()
# def Count_Line():
#     fp_r = open("SHIVAJI.TXT","r")
#     counter = 0
#     lineList = fp_r.readlines()
#     for i in lineList:
#         counter +=1
#     return counter

# print(Count_Line())
import pickle
def WRITERED():
    fp_w = open("PLANTS.dat","wb")
    id = input("Enter ID: ")
    nm = input("Enter Name: ")
    pr = input("Enter Price: ")
    userList = [id,nm,pr]
    pickle.dump(userList,fp_w)
    fp_w.close()

def SHOWHIGH():
    fp_r = open("PLANTS.dat","rb")
    while True:
        try:
            x = pickle.load(fp_r)
            if(int(x[0]) > 23):
                print(x)
        except EOFError:
            break
    
    fp_r.close()

menu = True

while menu:
    x = int(input("-->"))
    if(x == 1):
        WRITERED()
    elif(x == 2):
        SHOWHIGH()
    else:
        menu = False

# x = "Sreeejesh is beactyful"
# x= x.split()
# print(x)

# a = [1,2,3]
# b = ["a","b","c"]

# dic = {}

# for i in range(len(a)):
#     dic[a[i]] = b[i]

# print(dic)

# import random
# AR=[20,30,40,50,60,70]
# FROM=random.randint(1,3)
# TO=random.randint(2,4)
# for K in range(FROM,TO+1):
#  print(AR[K],end="#") 

# a= []
# p = str(a)
# k = int(a)
# print(k)


# mainStack = []

# getStr = input("Enter a string: ")
# for eachWord in getStr:
#     mainStack.append(eachWord)

# for i in range (len(mainStack)-1,-1,-1):
#     print(mainStack[i],end=" ")
    
