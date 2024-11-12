empty_var = ''
print(empty_var)

my_Cars =['BMW', 'LAMBO', 'TESLA', 'AUDI', 'BUGATI']
print(len(my_Cars))
print(my_Cars[0],my_Cars[3],len(my_Cars)-1)

#mixed data type
mixed_data_type =['Lotan',26,5.8,'Single',528]
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print('The number of campanies are:  ', len(it_companies))
print(it_companies[0],it_companies[3],it_companies[6])
it_companies[0] ='Meta'
print(it_companies)
it_companies.append('Microsoft')
print(it_companies)
it_companies.insert(4,'Microsoft')
print(it_companies)