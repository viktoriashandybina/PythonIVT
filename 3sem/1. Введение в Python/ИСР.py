print()
print('Задание №1.2')
print()

def sumarprog():
    i, summ, k, n = 0, 0, 5, int(input('Введите количество членов арифметической прогрессии: '))
    while i<n:
        summ = summ + k
        i += 1
    print('Сумма членов арифметической прогрессии = ', summ)

sumarprog()


print()
print('Задание №1.3')
print()
import math

def geron():
    a, b, c = int(input('Введите a: ')), int(input('Введите b: ')), int(input('Введите c: '))
    if a<=0 or b<=0 or c<=0:
        print('Введите значения больше 0!')
    else:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p -c))
        print('Площадь треугольника, вычесленная по формуле Герона = ' '%.3f' % s)

geron()


print()
print('Задание №1.4')
print()

a=float(input('Введите первое число: '))
b=float(input('Введите второе число: '))
c=str(input('Введите операцию: +,-,*,/  : '))

def calc(a,b,c):
    if c=="+":
        print(a+b)
        
    if c=="-":
        print(a-b)
        
    if c=="*":
        print(a*b)
        
    if c=="/":
        if b==0:
            print("Деление на 0! ")
        else:
            print(float(a/b))

calc(a,b,c)