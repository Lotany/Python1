name = 'lotan'
y =input("Whats your names :")

def compare_all():
    if y == name:
        print("Congartulations user")
    else:
        print("Th sysytem doesnt kow you!")

def move_forward():
    compare_all()
    if compare_all == True:
        y = input("Whats your age :")
        age =26
    else:
        print("You are not allowed to do this shit")

def final_verdict():
    move_forward()
    if move_forward == True:
        print("You have entered a favorite stage in life")
    else:
        print("What are you here for!!")

final_verdict()