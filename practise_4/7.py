# --coding: utf-8 --
s=input('Дана строка:')
s=s[:s.find('h')]+s[s.rfind('h')+1:]
print(s)