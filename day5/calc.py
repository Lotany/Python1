#simple calculator
print('Home Based Calculator')
first_number = float(input('Num 1:    '))
second_Number = float(input('Num 2:   '))
print('********Math********')
print('Select Math type \n ', '* - Multiply, \n / - divide \n - minus')
maths = input("Enter math sign:     ")
if maths == '*':
    print('Your answer is:  ',first_number*second_Number)
elif maths == '/':
    print('Your answer is:  ', first_number/second_Number)
elif maths == '-':
    print('Your answer i:  ',first_number-second_Number)
    