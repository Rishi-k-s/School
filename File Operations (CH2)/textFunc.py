
file_handle = open("D:\School\File Operations (CH2)\school_Dat.txt", "w+")
askDetails = ['School Name: ','Address: ',"phone no: ","email: "]
while True:
    try:
        getNumOfTimesToAddData = int(input('Enter the no. of times th evalue should be added:'))
    except:
        print("It should be a number")
        getNumOfTimesToAddData = int(input('Enter the no. of times th evalue should be added:'))
    for appendData in range (getNumOfTimesToAddData):
        getSchoolName = input(askDetails[0])
        getAddress = input(askDetails[1])
        getPhNo = input(askDetails[2])
        getEmail = input(askDetails[3])
        fullDetails = ['{} \n {}\n {} \n {}'.format(getSchoolName,getAddress,getPhNo,getEmail)]
        file_handle.writelines(fullDetails)
    break

