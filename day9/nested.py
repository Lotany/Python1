your_age =int(input("Enter your age: "))
my_age = 26
if my_age > your_age:
    minus = my_age -your_age
    if minus == 1:
        print("You are",minus, "year younger than me")
    else:
        print("You are",minus, "years younger than me")

else:
    my_age < your_age
    plus = your_age - my_age
    if plus == 1:
        print("You are", plus , "year older than me")
    else:
         print("You are", plus , "years older than me")
