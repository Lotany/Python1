def generate_full_name():
    first_name = 'Lotan'
    last_name = 'Kilinda'
    space = " "
    fullname = first_name + space + last_name
    print(fullname)
generate_full_name()

def sum():
    num1 = 2
    num2 = 2
    total = num1 + num2
    return total
print(sum())

def greetings (name):
    message = name + ", welcome to python"
    return message
print(greetings('Lotan'))

def sum_of_numbers(n):
    total =0
    for i in range(n+1):
        total +=i
    return total
print(sum_of_numbers(10))
print(sum_of_numbers(100))

def is_even(n):
    if n % 2 == 0:
        return True
    return False
print(is_even(7))


def even_nums(n):
    evens = []
    for i in range(n+1):
        if i % 2 ==0:
            evens.append(i)
    return evens
print(even_nums(10))

def greetings(name ='Lotan'):
    mess = name, ", Hello Sire"
    return mess
print(greetings('Lo'))