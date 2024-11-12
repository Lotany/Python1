#imserting item to a list
fruits = ['banana',['Orange'],['Mango'],['lemon']]
fruits.insert(0,'Tomoko')
print(fruits)

#remoiving item from a list
fruits.remove('banana')
print(fruits)

#using pop()
fruits.pop(0)
print(fruits)

#removing using del keyword\
del fruits[0:3]
print(fruits)

fruits = ['banana',['Orange'],['Mango'],['lemon']]
print(fruits)
#clean =fruits.clear()
#print(clean)

fruits_Copy = fruits.copy()
print(fruits_Copy)
fruits.append('tende')
print('**********')
print(fruits)
print(fruits_Copy)

#joing lists i python
positive_numbers =[1,2,3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers =negative_numbers + zero + positive_numbers
print(integers)

#using the extend function
num1 =[0,1,2,3,4]
num2 =[5,6,7,8,9]
num1.extend(num2)
print("*******")
print (num1)

#count method
fruits = ['banana','banana','Orange','Mango','lemon']
counter =fruits.count('banana')
print(counter)