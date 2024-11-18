neg ='123456789'
reverse =''
for i in range(len(neg),0,-1):
    reverse += neg[i-1]
print('The reverse of a number is = ',reverse)


n =7
for i in range(1,n+1):
    for j in range(i):
        print('#',end="")
    print()

