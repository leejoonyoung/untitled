# _*_ coding: utf-8 _*_
__author__ = 'jylee3'

tuple = (4, 5)
array = [1, 2]
map = {
    'name': 'lee',
    'age' : '11'
}
x, y = tuple

print "start out"
print tuple
print x
print y
print dict

with open('sample', 'rt') as f:
    data = f.read()
    print data

if False:
    print 'Hello 1'
print 'Hello 2'

sum = 0
for i in range(1, 11):
    sum = sum + i

print(sum)

