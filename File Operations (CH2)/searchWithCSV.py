import csv

get_userName = input("Enter the username you want to find: ")
get_psswrd = input("Enter the password you want to find: ")

file_handlr = open(r"File Operations (CH2)\userList.csv","r")
reader_file = csv.reader(file_handlr)
userNOtExists = False
userExists = False
for each_list in reader_file:
    if (each_list[0] == get_userName and each_list[1] == get_psswrd):
        print("********\nUsername: {}\nPassword: {}\nMail ID: {}\nPhonenumber: {}\n********".format(each_list[0],each_list[1],each_list[2],each_list[3]))
        userExists = True
    elif (each_list[0] == get_userName and each_list[1] != get_psswrd):
        print("Wrong passwd")
    elif (each_list[0] != get_userName):
        userNOtExists = True
if(userNOtExists == True and userExists == False):
    print("The user: {} does not exists".format(get_userName))
    
