print()
print("Задание 2")
print()
print(' '+ '_'*52)
print('| инструмент   ' + '| онлайн '+'| отображение предупреждений |')
print(' '+ '-'*52)
print('| pep8online   |'+ '   да   |'+'            да              |')
print('| pycodestyle  |'+ '  нет   |'+'           нет              |')
print('| atom-pep8    |'+ '  нет   |'+'            да              |')
print('| anaconda pep8|'+ '  нет   |'+'            да              |')
print(' '+ '-'*52)


print()
print("Задание 2.4")
print()
##Разработать программу, которая для заданного количества значений возвращала бы список из уникальных элементов, содержащихся во входном наборе значений

def unic(*l):
  n = []
  for i in l:
    if i not in n:
      n.append(i)
  return n

k=[1, 2, 3, 122, 1, 5000, 10, 1, -5434, 3, 4, 111, 4]
print(unic(k))


print()
print("Задание 2.5")
print()
#Реализуйте работу функции zip() через map()

list1=[1,2,3,4,5]
list2=[5,4,3,2,1]

print(list(zip(list1,list2)))
print(list(map(lambda x,y: (x,y), list1,list2)))