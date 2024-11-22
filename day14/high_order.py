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