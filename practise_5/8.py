# -- coding: utf-8 --
a = -1
c = 0
b = 0
n = int(input('Введите число:'))
while n != 0:
    if a == n:
        c =c + 1
    else:
        a = n
        b = max(b, c)
        c = 1
    n = int(input('Введите число:'))
b = max(b, c)
print(b)