# --coding: utf-8 --
n = int(input("Введите количество минут\n"))
h = n % (60 * 24) // 60
m = n % 60
print(h,":", m)
   