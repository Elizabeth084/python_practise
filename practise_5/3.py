# -- coding: utf-8 --
N = int(input('Введите число:'))
i = 1
m = 0
while i <= N:
    i = i*2
    m = m+1
    if i <= N:
        print(i, m)