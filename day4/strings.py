first_Name='Able'
last_Name='Kilinda'
language='python'
formated_String=('My name is %s %s. I teach %s' %(first_Name,last_Name,language))
print(formated_String)

#new style formating using .format()
formated_String=('My name is {} {}. I teach {} very well'.format(last_Name,first_Name,language))
print(formated_String)
a =4
b=3
print('{} + {} = {}'.format(a,b,a+b))

#string interpolation
print(f'{a} + {b} = {a+b} is the answer')

#strings as a sequence of characters
language ='Python'
a,b,c,d,e,f =language #unpacking sequence characers into variable
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#getting the last letter of the string
print('\n',language[0])
last_Letter=len(language)-1
last=language[last_Letter]
print(last)

#slicing a string in python
name_Lot='Lotany'
first_Three=name_Lot[0:3]
print(first_Three)

last_Three=name_Lot[3:6]
print(last_Three)


#Reversing a string
print(name_Lot[::-1])


#skipping characters while slicing
name_Real = 'Python'
pto=name_Real[0:6:4]
print('\n',pto)

#string methods
challange = 'thirty days of python' #coverts the first characterof the setence in capital
print(challange.capitalize())

#count() method
print(challange.count('y'))
print(challange.count('i'))

#endswith() method
print(challange.endswith('on'))
print(challange.endswith('in'))

mamu_Sh="thirty\tdays\tof\tpython"
print(mamu_Sh)
print(mamu_Sh.expandtabs(10))

print('\n')
challange = 'thirty days of python'
print(challange.find('f'))

print('\n')
print(challange.rfind('y'))
print('\n')
sub_String='ys'
print(challange.index(sub_String))
print('\n')
challange="ThirtyDaysPython"
print(challange.isalnum())
print('\n')

print(challange.isalpha())

print('\n')

print(challange.isdecimal())
num ='123'
print(num.isdecimal())

print('\n')
challange ='Thirsty'
print(challange.isdigit())
number='2345678'
print(number.isdigit())

web_tech =['HTML','JAVA','PYTHON']
result =' '.join(web_tech)
print(result)
print('\n')
challange ='thirty days of python'
print(challange.replace('python', 'java'))
print('\n')
print(challange.split(','))