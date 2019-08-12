#login = open("details.txt", "r")
#register = open("details.txt", "a")
print("1. Login as existing User")
print("2. Register as new User")
choice = int(input("Enter your choice [1 / 2] : "))

if(choice == 1):
    name = input("Enter Name ==>> ")
    password = input("Enter Password ==>> ")
    log = name+password
    login = open("details.txt", "r")
    login.seek(0)
    if(log in login.readlines()):
        print("Login Successful..")
        login.close()
    else:
        print("Wrong User Name or Password..")
        login.close()

elif(choice == 2):
    while(True):
        name1 = input("Enter Name ==>> ")
        password1 = input("Enter Password ==>> ")
        store = name1+password1
        login = open("details.txt", "r")
        register = open("details.txt", "a")
        login.seek(0)
        if(store in login.readlines()):
            print("Username already exists..\nTry Again..")
            continue
        else:
            register.write("\n"+store)
            print("Successfully registered..")
            register.close()
            login.close()
            break

#login.close()
#register.close()
