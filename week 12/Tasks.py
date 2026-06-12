b = {'CE','CS','CE','EE'}
b.add('AU')
print(b)

b.add('CE')
print(b)

b.discard('CS"')
print(b)

b.discard('CE')
print(b)

b.discard('VE"')
print(b)

b.remove('VE')
print(b)
