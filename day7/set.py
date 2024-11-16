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

#finding intersection items
whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_Numbers ={0,2,4,6,8,10}
print(whole_numbers.intersection(even_Numbers))

python = {'p','y','t','h','o','n'}
dragon = {'d','r','a','g','o','n'}
print(python.intersection(dragon))

print(whole_numbers.issubset(even_Numbers))

print(whole_numbers.issuperset(even_Numbers))

print(whole_numbers.difference(even_Numbers))

#finding the symetric dirrefence
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))

#joint or disjint sets
even_numbers1 = {0,9, 2, 4 ,6, 8}
odd_numbers2 = {1, 3, 5, 7, 9}
print(even_numbers1.isdisjoint(odd_numbers2))