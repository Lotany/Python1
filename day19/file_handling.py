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

import webbrowser
url_lists =[
    'http://www.python.org',
    'http://github.com/lotany',]

for url in url_lists:
    webbrowser.open_new_tab(url)

import requests # importing the request module

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page