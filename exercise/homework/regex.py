import re
test = '100-12345'
if re.match(r'^\d{3}\-\d{3,8}$', test):
    print('ok')
else:
    print('failed')

t ='ab c  d   e'.split() #切分
print('1',t)

t ='ab c  d   e'.split(' ')#
print('2',t)
print('3',re.split(r'\s+','ab c  d   e'))#\s+至少一个空格

m=re.match(r'^(\d{3})\-(\d{3,8})$','010-12345')
print('4',m.group(0))
print('5',m.group(1))
print('6',m.group(2))
