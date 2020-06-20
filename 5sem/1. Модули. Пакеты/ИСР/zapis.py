#Используется для записи одного гостя

import json

def newgost(i):
    a = ['id', 'name', 'sername', 'telnumber']
    new = dict.fromkeys(a)
    for key in list(new.keys()): 
        if key == 'id':
            new[key] = i
        if key == 'name':
            new[key] = input('Enter name: ')
        if key == 'sername':
            new[key] = input('Enter sername: ')
        if key == 'telnumber':
            new[key] = input('Enter telnumber: ')
    return new

with open('gostbook.json') as f:
    filename = json.load(f)

i = ((len(filename))+1)

filename.append(newgost(i))

with open('gostbook.json', 'w') as f:
    json.dump(filename, f)