import module
print(module.generate_full_name('Lotan','Kilinda'))

import sys
#print('Welcom {}. Enjoy {} challange!'.format(sys.argv[1],sys.argv[2]))

from statistics import *
ages =[20,20,4,24,25,22,26,20,23,22,26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

import math
print(math.pi)
print(math.sqrt(2))
print(math.pow(2,4))
print(math.floor(9.81))

#area of a circle
area = math.pi * 12*12
print(area)



import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

from random import random,randint
print(random())
print(randint(5,20))