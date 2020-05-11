print()
print('Задание 2.1')
print()
# 13.09.2018, Лабораторная работа 2
# Нужно сделать: конъюнкция, дизъюнкция и импликация

def AandB(a,b):
  return str(a and b)


def AorB(a,b):
  return str(a or b)


def AconseqB(a,b):
  return str(int(not a or b))


def table():
  print('-'*47)
  print('|  a  |  b  |  a and b  |  a or b  |  a => b  |')
  print('-'*47)
  for a in range(2):
    for b in range(2):
      print('|  '+str(a)+'  |  '+str(b)+'  |     '+AandB(a,b)+'     |     '+AorB(a,b)+'    |     '+AconseqB(a,b)+'    |')
  print('-'*47)

  
table()


print ()
print('Задание 2.2')
print()

def one(a,b,c):
  return (str(int((a and (b or c)) is ((a and b) or (a and c)))))

def two(a,c):
  return (str(int((not(a and (not c) or a) is not((not a) or c is c)))))


print ('                       Задание 18')
print ('–'*44)
print (chr(124) + ' A ' + chr(124) + ' B ' + chr(124) + ' C ' + chr(124) + '  A\/(B/\С)<->(A\/B)/\(A\/C)  ' +chr(124))
print ('–'*44)

for a in range(2):
    for b in range(2):
      for c in range(2):
        print (chr(124) + ' ' + str(int(a)) + ' ' + chr(124) + ' ' + str(int(b)) + ' ' + chr(124) + ' ' + str(int(c)) + ' ' + (chr(124)) + ' '*14 + str(one(a,b,c)) + ' '*15 + chr(124) + ' '*14  )
        print ('-'*44)




print ()
print ('                       Задание 23')
print ('–'*39)
print (chr(124) + ' A ' + chr(124) + ' C ' +  chr(124) + '  ' +chr(172)+ '(A)\/' + chr(172) + 'C/\A)<-> ' + chr(172) + '(' + chr(172) + 'A/\C->C)'+chr(124))
print ('-'*39)

for a in range(2):
  for c in range(2):
    print (chr(124) + ' ' + str(int(a)) + ' ' + chr(124) + ' ' + str(int(c)) + ' ' + (chr(124)) + ' '*14 + str(two(a,c)) + ' '*14 + chr(124) + ' '*14  )
    print ('-'*39)







print ()
print('Задание 2.3')

lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]

print ()
print ('                       Задание №10')
l1 = (lst[1:len(lst)//2])
print (l1[-1]*(-1))



print ()
print ('                       Задание №16')

s = 0
l2 = (lst[0:len(lst):2])
for i in l2:
  s = s+i
print (s)
print (min(lst))


print ()
print('Задание 2.4')
print ()

def sqare(a,b,h):
  s=a*b+a*h+b*h+((a**2+b**2)**0.5)*h
  print('Площадь поверхности треугольной призмы =', '%.3f' % s)

a=float(input('Введите а: '))
b=float(input('Введите b: '))
h=float(input('Введите h: '))

if a==0 or b==0 or h==0:
  print('Введите значения больше 0!')
else:
  sqare(a,b,h)

  print('\n')