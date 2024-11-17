#while loop
count = 0
while count < 5:
    #print(count)
    count = count + 1
    if count ==3:
        continue
    print(count)
print("********************************")

#for loop with list
numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)

#for loop with string
name = "lotan"
for n in name:
    print(n)
print("############################")
for i in range(len(name)):
    print(name[i])
#for loop with tuple
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)

#for loop in dictionary

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

#range
lst = list(range(11))
print(lst)

st =set(range(1,11))
print(st)

lst =list(range(0,20,3))
print(lst)

#nested loop
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key =='skills':
        for skill in person['skills']:
            print(skill)
#for else
for number in range(11):
    print(number)
else:
    print('The loop stops at',number)


for num in range(6):
    pass