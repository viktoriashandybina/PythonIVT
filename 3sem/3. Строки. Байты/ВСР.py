print()
print("Задание 2")
print()
import random
rmin = 0
rmax = 99
rand = random.randint(rmin, rmax)
print("Я сгенерировал случайное число от {} до {}.Попробуй угадать.".format(rmin, rmax))
while True:
    try:
        prompt = int(input("Угадай число: "))
        if prompt != rand:
            if prompt < rand:
                print("Твое число меньше")
            if prompt > rand:
                print("Твое число больше")
        else:
            break
    except ValueError:
        print("Вы ввели не число")
print("Правильно! Это число {}".format(rand))



print()
print("Задание 3")
print()
for i in range(65, 123):
    if i not in range(91, 97):
        print(chr(i), end='')
print()
for i in range(1040, 1104):
    print(chr(i), end='')
print()