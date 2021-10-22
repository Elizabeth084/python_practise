# --coding: utf-8 --
s=input('Дана строка:')
s1 = s[:s.find('h')] 
s2 = s[s.find('h'):s.rfind('h') + 1]
s3 = s[s.rfind('h') + 1:]
print( s1 + s2[::-1] + s3)
