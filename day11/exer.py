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

def convert_temp(temp):
    fah = (temp*9/5)+32
    return fah
print('Farrent is: ',convert_temp(10))

def check_season(month):
    if month == "september" or "october" or "november":
        return print("The season is Autum")
    elif month =="december" or "january" or "february":
        print("the season is Winter")
    elif month =="march" or "april" or "may":
        print("the season is Spring")
    elif month=="june" or "july" or "august":
        print("The season is Summer")
print(check_season("september"))