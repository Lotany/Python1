#function as parameters
def sum_numbers(nums):
    return sum(nums)

def high_order_function(f,lst):
    summation =f(lst)
    return summation
result = high_order_function(sum_numbers,[1,2,3,4,5])
print(result)

def square(x):
    return x**2
def cube(x):
    return x**3
def absolute(x):
    if x >=0:
        return x
    else:
        return -(x)
def high_order_function(type):
    if type == 'square':
        return square
    elif type =='cube':
        return cube
    elif type =='absolute':
        return absolute
result =high_order_function('square')
print(result(3))
result = high_order_function('cube')
print(result(3))
result =high_order_function('absolute')
print(result(3))

def add_ten():
    ten =10
    def add(num):
        return num + ten
    return add
closure_result =add_ten()
print(closure_result(5))

#decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to python'
print(greeting())

def decorator_function(func):
    def warapper_funtion():
        return func()
    return warapper_funtion

@decorator_function
def display():
    print('The display function was called')
display()

import functools

def decoratorFunction(func):
    @functools.wraps(func)
    def wrapperFunction(*args, **kwargs):
        print('Wrapper executed before {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapperFunction

@decoratorFunction
def display():
    print('The display function was called')

@decoratorFunction
def display_info(name, age):
    print('display_info was called with ({}, {})'.format(name, age))

display_info('Kalam', 83)  
display()




def my_fam(function):
    def wrapper(brother,age,work):
        function(brother,age,work)
        print('My brother is called {}, he is {} years old and works at {}'.format(brother,age,work))
    return wrapper

@my_fam
def display(brother,age,work):
    print('Hello')
display('Tony','20','kenyapower')



#map function
numbers =[1,2,3,4,5,6]
def square(x):
    return x**2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

#map function using lambda
numbers_squared = map(lambda x : x**2, numbers)
print(list(numbers_squared))

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper, names)

from datetime import datetime
now = datetime.now()
print(now)
day =now.day
month =now.month
year =now.year
hour = now.hour
minute =now.minute
second =now.second
timestap =now.timestamp()
print(day,month, year, hour, minute)
print('timestap', timestap)
print(f'{day}/{month}/{year}, {hour}:{minute}')


var =10
var1 ='5'
try:
    result = var + var1
    print(result)
except:
    print("Something went wrong")


""""
try:
    name =input('Enter your name')
    year_born = input('year your born')
    age =2024 -year_born
    print(f'Your name is {name}. And you are {age} years old')
except Exception as e:
    print(e) """
def sum(a,b,c,d,e,g,y):
    return a+b+c+d+e+g+y 

lst = [1,2,3,4,5,67,8]
print(sum(*lst))

def sum(*args):
    s=0
    for i in args:
        s +=1
    return s
print(sum(1,2,3))
