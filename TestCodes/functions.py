"""def addSubMulDiv(num1,num2):
    add = num1+num2
    sub = num1-num2
    mul = num1*num2
    divd = num1/num2
    return(add,sub,mul,divd)
addNum,subNum,multNum,divNum = addSubMulDiv(10,20)
print(addNum,subNum,multNum,divNum)
"""
def checkDivisible(num1,num2):
    if(num1%num2 == 0 ):
        return True
    else:
        return False

def listWherValAreSqNosBetwn1Nd30 ():
    sqList = []
    for i in range(1,31):
        sqList.append(i**2)
    return sqList

def recursivSumOfNos (num):
    if num == 0:
        return 0
    else:
        return(num**2+recursivSumOfNos(num-1))