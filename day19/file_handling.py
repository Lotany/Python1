f = open('./files/reading_file_example.txt')
txt = f.read(3)
print(txt)
f.close()

f1=open('./files/reading_file_example.txt')
line = f1.readlines()
print(line)
f1.close()

with open('./files/reading_file_example.txt') as f:
    lines =f.read()
    print(lines)