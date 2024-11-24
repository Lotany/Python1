def linear_search(list, target):
    """
    returns the index position of the target if found, else retuns none
    """
    for i in range(0, len(list)):
        if list[i] ==target:
            return i
    return None
#verify function if the value is not none it informs the value of the position if not
#it was not found on the list
def verify(index):
    if index is not None:
        print("Target found at index", index)
    else:
        print("Target not found")
numbers =[1,2,3,4,56,7,8,9,10]
result =linear_search(numbers,12)
verify(result)

result =linear_search(numbers,3)
verify(result)