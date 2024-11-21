#function as parameters
def sum_numbers(nums):
    return sum(nums)

def high_order_function(f,lst):
    summation =f(lst)
    return summation
result = high_order_function(sum_numbers,[1,2,3,4,5])
print(result)