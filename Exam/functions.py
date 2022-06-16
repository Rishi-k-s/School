
def printit(list2):
    m=n =  list2[0]
    for a in list2:
        if a<n:
            n=a
        if a>m:
            m=a
        print(m,n)
list