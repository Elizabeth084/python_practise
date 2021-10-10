# --coding: utf-8 --
n = int(input('Введите количество чисел: '))
a1 = 0
a2 = 1
m = 0
sum = 1
if n >= 3:
    for i in range(n - 2):
        m = a1 + a2
        sum = sum + m
        a1 = a2
        a2 = m
    print(sum)
