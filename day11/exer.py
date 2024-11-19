def add_two_numbers(num1,num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(10,10))

def area_circle(r):
    pi =3.14
    area = pi *r**2
    return area
print(area_circle(4))

def add_all_numbers(*args):
    sum = 0
    for arg in args:
        sum +=arg
        if int(sum) == True:
            print("Its an integer")
        else:
            print("its anumber")
    return sum
print(add_all_numbers(2,2,2,2,2))