import csv

file_handlr = open(r"File Operations (CH2)\userList.csv","a+",newline='\n')
writer_file = csv.writer(file_handlr,)
reader_file = csv.reader(file_handlr)

createUsersBool = True
readUserBool = True

def createUserCSV (getNoOfUserToAdd):
    userCounter=1
    header_add = writer_file.writerow(['name','password','Mail ID','Phone No.'])
    for each_user in range(getNoOfUserToAdd):
        username_gettr = input("Name of user {}: ".format(userCounter))
        password_check = True
        while password_check:
            password_gettr = input("what is your Password: ")
            passwrd_confrm_gettr = input("re-enter your Password: ")
            if(password_gettr == passwrd_confrm_gettr):
                password_check =False
            else:
                print("**The passwords doesn't Match**")
        mailID_gettr = input("Enter your E-mail ID: ")
        phone_gettr = input("what is your Phone no: ")
        user_Details_List = [username_gettr,password_gettr,mailID_gettr,phone_gettr]
        writer_file.writerow(user_Details_List)
        userCounter +=1

def searchUserCSV(userName,psswrd):
    userNOtExists = False
    userExists = False
    for each_list in reader_file: 
        if (each_list[0] == userName and each_list[1] == psswrd):
            print("********\nUsername: {}\nPassword: {}\nMail ID: {}\nPhonenumber: {}\n********".format(each_list[0],each_list[1],each_list[2],each_list[3]))
            userExists = True
        elif (each_list[0] == userName and each_list[1] != psswrd):
            print("Wrong passwd")
        elif (each_list[0] != userName):
            userNOtExists = True
    if(userNOtExists == True and userExists == False):
        print("The user: {} does not exists".format(userName))

get_createOrSearchUser = int(input("1 => Create user\n2 => Search User\n3 => Quit\n=>"))

if (get_createOrSearchUser == 1):
    while createUsersBool: 
        getNoOfUsers = int(input("How many users u want to add: "))
        createUserCSV(getNoOfUsers)
        try:
            wantToAddMoreUserCheck = bool(input("Case-sensitive input\nWant to add more users(True/False)?: "))
            if(wantToAddMoreUserCheck == True):
                createUsersBool = True
            elif(wantToAddMoreUserCheck == False):
                createUsersBool = False
                break
        except:
            print("Try again :)")            
elif (get_createOrSearchUser == 2):
    while readUserBool:
        get_userName = input("Enter the username you want to find: ")
        get_psswrd = input("Enter the password you want to find: ")
        searchUserCSV(get_userName,get_psswrd)
        try:
                wantToReadMoreUserCheck = bool(input("Case-sensitive input\nWant to read more users(True/False)?: "))
                if(wantToReadMoreUserCheck == True):
                    readUserBool = True
                elif(wantToReadMoreUserCheck == False):
                    readUserBool = False
        except:
                print("Try again :)") 
    print("-Goodbye-")
elif(get_createOrSearchUser == 2):
    print("-Goodbye-")
else:
    print("Run the Code again")
    
file_handlr.close()