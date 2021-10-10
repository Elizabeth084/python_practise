# --coding: utf-8 --
a = int(input("Введите число\n"))
b = int(input("Введите число\n"))
for i in range(a +a % 2-1, b - 1, -2):
  print(i, end=' ') 