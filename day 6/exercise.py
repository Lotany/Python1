tpl =()
sibling_brothers = ('Alex','Lotan','Tony')
sibling_sisters = ('Edith','Sharon','Bety')
siblings = sibling_brothers + sibling_sisters
print('I have',len(siblings),'siblings they are as follows')
print(siblings)
modify =list(siblings)
modify.insert(0,'Kilinda')
modify.insert(1,'Juliana')

familly_members = tuple(modify)
print(familly_members)
(sibling) =familly_members
print('$$$$$$$$$$$$$$$$$')
print(sibling)
fruits = ('banana','mango')
vegetables =('kales','Spinach')
animal_product = ('Meat','eggs','Soup')
food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)
food_stuff_lt =list(food_stuff_tp)
sliced =food_stuff_lt[3:-3]
print(sliced)
convert =tuple(food_stuff_lt)
del convert
del1 = 'Soup' in convert
print(del1)
