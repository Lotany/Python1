number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
number3=int(input("Enter the third number: "))

largest_no = number1
if number2 >largest_no:
    largest_no =number2
    
if number3>largest_no:
    largest_no =number3

print("The largest number is, ",largest_no)