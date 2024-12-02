secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess =int(input("Enter you number: "))
count = 3
while count:
    count +=1
    if guess ==secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        if guess < secret_number:
            print("The number is above than")
        else:
            print("The number is below that:Keep trying")
        print("You are stuck in my loop now!!")
        guess =int(input("Enter you number: "))

        