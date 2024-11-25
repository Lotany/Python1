f = open('./files/reading_file_example.txt')
txt = f.read(3)
print(txt)
f.close()

f1=open('./files/reading_file_example.txt')
line = f1.readlines()
print(line)
f1.close()



#appending a new text
with open('./files/reading_file_example.txt','a') as g:
    g.write('This text has to be appended')

with open('./files/reading_file_example.txt') as f:
    lines =f.read()
    print(lines)