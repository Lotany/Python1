person = {'first_name':'Lotan','second_name':'Maghanga','Age':'26','country':'Kenya','is_married':False,'skills':['Python','React'],'Adress':{'Physical_ad':'Kilifi','Box_no':'528'}}

print(person['Adress'])
person['Job_tile'] = 'Sales_DSR'
print(len(person))

person['skills'].append('Java')
print(person)