user = ''
paswd = ''

print('Welcome to my program')

def quiz():
     print("Hello boy")

def login():
        user = input("Set your username: ")
        paswd = input("Enter password: ")
        trial = 3
        while trial <=3:
            passwdtype = len(paswd)
            if passwdtype<5:
                trial +=1
                paswd = input("Enter password: ")
            else:
                print("Profile created successfully")
                quiz()
                break
login()



