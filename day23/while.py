import time
start = time.time()
no =0
while no <=100:
    no +=1
    print(no, sep=' ', end='', flush=True)
    print(no)
    time.sleep(2)
end = time.time()
print("The execution time of the above proram is :",(end-start)*10**3, "ms")
