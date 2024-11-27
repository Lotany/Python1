class Person:
    def __init__(self,firstname,lastname,country):
        self.firstname = firstname
        self.lastname = lastname
        self.country =country

    def personal_info(self):
        return print('My name is ',p.firstname, p.lastname, 'I am from ',p.country)
p =Person('Lotan','Kilinda','Kenya')
print(p.personal_info())

#objects can have methods - methods are functions wich belong to the object

#object default methods
class Person:
    def __init__(self,firstname='Tony',lastname='Kilinda',residence='Mombasa'):
        self.firstname=firstname
        self.lastname =lastname
        self.residence=residence
        self.skills =[]

    def more_Details(self):
        s='My name is, '
        m = ' I am from '
        p = print(s,self.firstname,self.lastname,m,self.residence)
        return p
    def adds_skill(self,skill):
        self.skills.append(skill)
p =Person()
print(p.more_Details())
p.adds_skill('HTML')
p.adds_skill('CSS')
p.adds_skill('JAVASCRIPT')
p1 =Person('Lotan','Kilinda','Mombasa')
print(p1.more_Details())
print(p.skills)
