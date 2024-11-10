first_Name='Able'
last_Name='Kilinda'
language='python'
formated_String=('My name is %s %s. I teach %s' %(first_Name,last_Name,language))
print(formated_String)

#new style formating using .format()
formated_String=('My name is {} {}. I teach {} very well'.format(last_Name,first_Name,language))
print(formated_String)