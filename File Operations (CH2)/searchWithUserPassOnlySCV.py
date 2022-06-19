import csv

# file methords
try:
    file_handlr = open(r"File Operations (CH2)\userPasswd.csv","r+",newline='\n')
except:
    file_handlr = open(r"File Operations (CH2)\userPasswd.csv","w",newline='\n')

writer_file = csv.writer(file_handlr)
reader_file = csv.reader(file_handlr)

#boolians
createUsersBool = True
readUserBool = True

#function to create user and add it to CSV file functions
def createUserCSV (getNoOfUserToAdd):
    userCounter=1
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
        user_Details_List = [username_gettr,password_gettr]
        writer_file.writerow(user_Details_List)
        userCounter +=1

#function to read user details from CSV file
def searchUserCSV(userName):
    userNOtExists = False
    userExists = False
    for each_list in reader_file:
        if (each_list[0] == userName):
            print("********\nUsername: {}\nPassword: {}\n********".format(each_list[0],each_list[1]))
            userExists = True
        elif (each_list[0] != userName):
            userNOtExists = True
    if(userNOtExists == True and userExists == False):
        print("The user: {} does not exists".format(userName))

#Starting menu
get_createOrSearchUser = int(input("1 => Create user\n2 => Search User\n3 => Quit\n=>"))

#menu functions
if (get_createOrSearchUser == 1): #Creating user
    while createUsersBool == True: 
        getNoOfUsers = int(input("How many users u want to add: "))
        createUserCSV(getNoOfUsers)
        try:
            wantToAddMoreUserCheck = input("Want to add more users(y/n)?: ")
            if(wantToAddMoreUserCheck == 'y'):
                createUsersBool = True
            elif(wantToAddMoreUserCheck == 'n'):
                createUsersBool = False
        except:
            print("Try again :)")  
    print("-Goodbye-")          
elif (get_createOrSearchUser == 2): #Searching user
    while readUserBool == True:
        get_userName = input("Enter the username you want to find: ")
        searchUserCSV(get_userName)
        wantToReadMoreUserCheck = input("Want to read more users(y/n)?: ")
        if(wantToReadMoreUserCheck == 'y'):
            readUserBool = True
        else:
            readUserBool = False
    print("-Goodbye-")
elif(get_createOrSearchUser == 3):
    print("-Goodbye-")
else:
    print("Run the Code again")

file_handlr.close()