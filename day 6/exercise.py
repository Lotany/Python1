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