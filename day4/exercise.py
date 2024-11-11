word1='Thirty'
word2 ='Days'
word3='Of'
word4='Python'
learn=word1+ ' ' +word2+ ' ' + word3+' ' +word4
print(learn) 

code1='Coding'
code2='For'
code3='All'
codes = code1+' '+code2+ " "+" "+code3
print(codes)

company='Coding For All'
print(company)
print(len(company))
upper =company.upper()
print(upper)
lower =company.lower()
print(lower)

print('*******************')
capital = company.capitalize()
capital0 =company.swapcase()
capital2 =company.title()
print(capital,'\n',capital0, '\n', capital2)


slicer = len(company)
print(slicer)
sliced = company[6:slicer]
print('@@@@@@@@@')
print(sliced)

finer = company.find('Coding')
print(finer)

finding = 'Coding'
print('\n')
print(company.index(finding))

print(company.replace('Coding', 'Python'))

every_One= 'Pythone for everyone'
print(every_One.replace(every_One,"Python for all"))
print('________')
print(every_One.split( ))


major_Companies= 'Facebook,Google,Microsot,apple, ibm, Oracle'
print(major_Companies)
print(major_Companies.split(','))

print(len(company)-1)
pto=company[0],[6],[11]
print(pto)

print(company.rindex('i'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

print(sentence.rfind('because'))
phrase = 'you cannot end a sentnce with because because because is a conjuction'
print(phrase.index('b'))
sli = phrase[30:52]
print(sli)
print(phrase)
