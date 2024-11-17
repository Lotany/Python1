import getpass
user_access =1
login = 0
pass_word = "1234"
user_name = 'lotan'

user_log_name = input("Enter your username to login: ")
if user_log_name == user_name:
    print("Enter Passwword to login")
    user_log_password = input("Enter Password to continue: ")
    if user_log_password == pass_word:
        print("**************************************************")
        print("**\tkindly select the following options\t**")
        print("**\t\t \t\t\t\t**")
        print("**\t\t key\t\tvalue\t\t**")
        print("**\t\t1\t\tJAN\t\t**")
        print("**\t\t2\t\tFEB\t\t**")
        print("**\t\t3\t\tMARCH\t\t**")
        print("**\t\t4\t\tAPRIL\t\t**")
        print("**\t\t5\t\tMAY\t\t**")
        print("**\t\t6\t\tJUNE\t\t**")
        print("**\t\t7\t\tJULY\t\t**")
        print("**\t\t8\t\tAUGUST\t\t**")
        print("**\t\t9\t\tSEPTEMBER\t**")
        print("**\t\t10\t\tOCTOBER\t\t**")
        print("**\t\t11\t\tNOVEMBER\t**")
        print("**\t\t12\t\tDECEMBER\t**")
        print("**************************************************")
        select_option = int(input("Enter your month"))
        if select_option == 1:
            print("Here are the records for Jan")
    else:
        print("Incorrect password or password try again!!!!")