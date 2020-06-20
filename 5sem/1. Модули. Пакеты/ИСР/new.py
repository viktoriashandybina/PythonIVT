#Здесь создается "Список гостей", не использовать для записи одного гостя в существующий json файл!! 
#При попытке записать одного гостя удалятся все существующие, т.к. программа создает именно первоначальный список, с которым потом можно работать

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

b = []
x = None
i = 0
while x != 'no':
    i += 1
    x = str.lower(input('Вы хотите добавить человека?(yes/no): '))
    if x == 'yes' or x == 'no':
        if x == 'yes':
            b.append(newgost(i))
        if x == 'no': 
            print('Ввод закончен')
            break
    else:
        print('Вы ввели неправильно')

new = b
with open('gostbook.json', 'w') as f:
    json.dump(new, f)