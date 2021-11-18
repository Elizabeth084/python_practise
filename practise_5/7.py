# -- coding: utf-8 --
n = int(input('Введите число:'))
i = 0
while n != 0:
    a = int(input('Введите число:'))
    if (a != 0) and (n < a):
        i += 1
    n = a
print(i)