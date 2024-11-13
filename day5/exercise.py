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
front_end =['HTML', 'CSS', 'JS', 'REACT', 'REDUX']
back_end= ['Node', 'Express', 'MongoDB']
prog_languages = front_end + back_end
print(prog_languages)
print("*************************")
front_end.extend(back_end)
print(front_end)

ages =[19,22,19,24,20,25,26,24,25,24]
ages.sort()
print(ages)
print('*************')
print(ages)
min_Age = min(ages)
max_age = max(ages)
print('The  mean and max age include : ', min_Age, max_age)
n =len(ages)
ages.sort()
if n % 2 == 0:
    median1 = ages[n//2]
    median2 = ages[n//2 -1]
    median = (median1+median2)/2
else:
    median = n[n//2]
print("Median is: " + str(median))