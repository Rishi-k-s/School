
with open("D:\School\File Operations (CH2)\school_Dat.txt", "r+") as file_handle:
    askDetails = ['School Name: ','Address: ',"phone no: ","email: "]
    askNumCheck = True
    while True:
        while askNumCheck:
            try:
                getNumOfTimesToAddData = int(input('Enter the no. of times th evalue should be added:'))
                askNumCheck = False
            except:
                print("It should be a number")
                askNumhkeck = True
        for appendData in range (getNumOfTimesToAddData):
            getSchoolName = input(askDetails[0])
            getAddress = input(askDetails[1])
            getPhNo = input(askDetails[2])
            getEmail = input(askDetails[3])
            fullDetails = ['{}\n{}\n{}\n{}'.format(getSchoolName,getAddress,getPhNo,getEmail)]
            file_handle.writelines(fullDetails)
        wantToRead = input('Want to Read (yes/no):')
        if wantToRead == 'yes':
            for lines in file_handle:
                print(file_handle.read())
            break
        else:
            break