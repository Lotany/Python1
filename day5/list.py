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

#unpacking list items using *rest
fruits=['banana', 'orange', 'mango','lemon','lime','apple']
fruit1,fruit2,fruit3, *rest =fruits
print(rest)

first, second, third, *rest, tenth =[1,2,3,4,5,6,7,8,9,10]
print(rest)

countries = ['Germany', 'France','Belgium', 'Sweden','Denmark','Finland', 'Norway','Iceland','Estonia']
gr,fr,bg,sw, *scan, es =countries
print(gr)
print(scan)

#slicing list items from a list
fruits=['banana', 'orange', 'mango','lemon','lime','apple']
all_Fruits = fruits[0:4]
print('*********************')
print(all_Fruits)
lemo = fruits[::7]
print("@@@@@@@@@@@")
print(lemo)

#modifying list
fruits=['banana', 'orange', 'mango','lemon','lime','apple']
fruits[-1] = "Lotan"
print(fruits)
does_exist = 'banana' in fruits
print(does_exist)

fruits=['banana', 'orange', 'mango','lemon','lime','apple']
mendy =fruits.append('kilifi')
kilif- = 
print(mendy)