person = {'first_name':'Lotan','second_name':'Maghanga','Age':'26','country':'Kenya','is_married':False,'skills':['Python','React'],'Adress':{'Physical_ad':'Kilifi','Box_no':'528'}}

print(person['Adress'])
person['Job_tile'] = 'Sales_DSR'
print(len(person))

person['skills'].append('Java')

print('first_name' in person)
print(person.pop('first_name'))
print(person.popitem())
del person['is_married']
print(person)
print(person.items())
#print(person.clear())
keyla =person.keys()
print(keyla)
vally = person.values()
print('**********************')
print(vally)