import csv

fp = open("usr_pswd.csv", "w", newline='\n')
fp.close()

def adduser(usr_list):
    add_fp = open("usr_pswd.csv","a",newline='\n')
    writer_obj = csv.writer(add_fp)
    writer_obj.writerow(usr_list)
    print("User Added")
    add_fp.close()


def search():
    reader_fp = open("usr_pswd.csv", "r", newline='\n')
    reader_obj = csv.reader(reader_fp)
    name = input("Enter name to search:")
    user_found = False
    user_not_found = False
    for row in reader_obj:
        if row[0] == name:
            user_found = True
            print("User Name : ", row[0], "\nPassword : ", row[1])
        elif row[0] != name:
            user_not_found = True
    if user_found == False and user_not_found == True:
        print(name, " not found")
    reader_fp.close()


c = 'y'
while c == 'y' or c == 'Y':
    choice = int(input("1. Add User\n2. Search User\n3. Exit\nEnter your choice:"))

    if choice == 1:
        ch = 'y'
        while ch == 'y' or ch == 'Y':
            name = input("Enter User Name: ")
            password = input("Enter Password: ")
            adduser([name, password])
            ch = input("Do you want to add more user(y/n) : ")

    elif choice == 2:
        search()
    elif choice == 3:
        print("Program Completed")
        exit(0)
    c = input("Do you want to perform more operation(y/n) : ")