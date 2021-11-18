# -- coding: utf-8 --
s = 0
l = 0
n= int(input('Введите число:'))
while n != 0:
    s = s + n
    l = l + 1
    n = int(input('Введите число:'))
print(s / l)