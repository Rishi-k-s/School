"""def addSubMulDiv(num1,num2):
    add = num1+num2
    sub = num1-num2
    mul = num1*num2
    divd = num1/num2
    return(add,sub,mul,divd)
addNum,subNum,multNum,divNum = addSubMulDiv(10,20)
print(addNum,subNum,multNum,divNum)
"""
def Revert(Num,Last=2):
    if Last%2==0:
        Last=Last+1
    else:
        Last=Last-1
    for C in range(1,Last+1):
        Num+=C
    print(Num)
A,B=20,4
Revert(A,B)
B=B-1
Revert(B)

