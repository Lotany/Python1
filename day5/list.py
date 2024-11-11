fruits =['Banana', 'Mango', 'Orange','Lemon']
vegetables = ['Tomato','Potato', 'Cabbage', 'Onion', 'Carrot']

print('Fruits:',fruits)

#positive indexing
first_Fruit=fruits[3]
last_Fruit = len(fruits)-1
print(first_Fruit)
print(last_Fruit)

#negative indexing
nega_Tive = fruits[-1]
print(nega_Tive)

fruits=['banana', 'orange', 'mango','lemon','lime','apple']
fruit1,fruit2,fruit3, *rest =fruits
print(rest)