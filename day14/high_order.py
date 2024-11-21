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