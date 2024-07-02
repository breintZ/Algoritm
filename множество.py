'''
s = set('myrlo')
t = set([1, 10, 23])
s.add('v')
print(s | t)
print(s ^ t)
print(t - s)
print(t & s)
print('y' in s)
print(t.__len__())


def add(s, t):
    s = set('myrlo')
    t = 'www'
    return s.add(t)
print(add(['myrlo'], ['www']))

def double(num):
    """Функция, которая удваивает значение"""
    return 2*num
print(double.__doc__)
'''

import math

a = math.sqrt(2)

print('%20s' %a)
