#creating an empty tuple
tpl =('item 1', 'item 2', 'item 3')
fruits =('banana', 'orange', 'mango', 'lemon')
print(fruits)
lengthy = len(fruits)
print(lengthy)

#accesing tuple items using positive and negative indexing
#positive indexing
fist_item =fruits[0]
print(fist_item)
last_item = fruits[-1]
print(last_item)
print("*******************")
last_index = len(fruits) -1
lasty_item = fruits[last_index]
print(lasty_item)
print('####################')
all_fruits = fruits[0-4]
print(all_fruits)
all_fruits =fruits [0:]
print(all_fruits)
first_fruit =fruits[1:3]
print(first_fruit)

ferit = fruits[-3]
print(ferit)


#changing tuple to lists
lst = list(fruits)
lst.append("Kiwi")
tp = tuple(lst)
print(tp)

#checking item in a tuple
'''
onfirm = 'orange' in fruits
oranges =10
if onfirm == True:
    print("how many oranges do you want?")
    get_oranges = int(input(" Enter the number of oranges : "))
    if get_oranges > 10:
        print('Out of oder, Kindly wait for the next season')
    else:
        print('Congatulation your order of', get_oranges, 'has been deliverd')
else:
    print("We are sad to know that you havent purchased any fruits, Thank you")
'''
#joining a tuple
tp1 =('item1','item2','item3')
tpl2 =('item4','item5','item6')
tpl3 =tpl+tpl2
print(tpl3)

#deleting a tuple 
'''del tpl3
print(tpl3)'''
