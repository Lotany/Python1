class Person:
    def __init__(self,firstname,lastname,country):
        self.firstname = firstname
        self.lastname = lastname
        self.country =country
p =Person('Lotan','Kilinda','Kenya')
print('My name is ',p.firstname, p.lastname, 'I am from ',p.country)