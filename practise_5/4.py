# --coding: utf-8 --
x=int(input('Введите число:'))
y=int(input('Введите число:'))
d = 1
while x<y:
    x = x + (x * 0.1)
    d=d+1
print(d)
     