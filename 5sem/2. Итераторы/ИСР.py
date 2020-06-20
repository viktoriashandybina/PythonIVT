#Разработать функцию, возвращающую элементы ряда Фибоначчи по данному максимальному значению.

def fib(n):
  fib1=0
  fib2=1
  print(fib1,fib2, end=" ")
  while fib2<n :
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    if fib2>n: break
    print(fib2, end=" ") 
    
fib(int(input('Введите число:  '))) 




#Создание программы, возвращающей список чисел Фибоначчи с помощью итератора.

class Fib:
  def __init__(self, k):
    self.k = k

  def __iter__(self):                           
    self.fib1 = 0
    self.fib2 = 1
    print(self.fib1, self.fib2, end=" ")
    return self

  def __next__(self):
    fib_sum = (self.fib1 + self.fib2)
    self.fib1 = self.fib2
    self.fib2 = fib_sum
    if fib_sum > self.k:
      raise StopIteration 
    return fib_sum

for i in Fib(int(input("\nВведите число:  "))):
  print (i, end=" ")