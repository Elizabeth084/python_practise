# --coding: utf-8 --
s=input('Дана строка:')
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'),s.rfind('f'))