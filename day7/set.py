#creating an empty set
fruits = {'banana','orange','mango','lemon'}

#getting th set length
lengthy = len(fruits)
print(lengthy)

#accessing items in a set
#refer to he loop section

#checking an item using in
print('Does the set contain orange', 'orange' in fruits)

#adding items to  a set
fruits.add('Kiwi')
print(fruits)

#adding multiple items using update
fruits.update(['tomato','passion','tomoko','apple'])
print(fruits)
#removing an item from aset
fruits.remove('orange')
print(fruits)
fruits.pop()
print(fruits)
#clearing items from a set
'''fruits.clear()
print(fruits)'''

#deleting a set
'''del fruits
print(fruits)'''

#converting list to set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}

#joining sets
fruits ={'banana','oramge', 'mango', 'lemon'}
vegetables = { 'tomato','spinach','cabbage'}
print(fruits.union(vegetables))

fruits.update(vegetables)
print("****************")
print(fruits)