# --coding: utf-8 --
s=input('Дана строка:')
b=int(s.find(' '))+1
a=int(len(s))
c=str(s[b:a])+str(' ')+str(s[:b])
print(c)