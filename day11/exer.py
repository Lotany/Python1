import sys
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
        print("The season is Autum")
        return
print(check_season("october"))

# Python program for slope of line 
def slope(x1, y1, x2, y2): 
    if(x2 - x1 != 0): 
      return (float)(y2-y1)/(x2-x1) 
    return sys.maxint 
  
  
# driver code 
x1 = 4
y1 = 2
x2 = 2
y2 = 5
print ("Slope is:", slope(x1, y1, x2, y2))


# function print_list
# accepts a list as parameter
def print_list(input_list):
    # for loop to access each element 
    for each_item in input_list:
        # print 
        print(each_item)


def reverse_list(arr):
    result = []
    
    for i, _ in enumerate(arr):    # try to use enumerate - it's better in most cases
        result.append(arr[~i])     # use the backward indexing here
        
    return result