import random as rn
"""
def intHash (key : int, size : int):
    return key % size
"""
def numberHash (key : int, size : int):
    s = str (key)
    sum = 0
    m = 1
    for digit in s:
        sum += m * int(digit)
        m += 1
    return sum % size

def stringHash(key : str, size):
    sum = 0
    for s in key:
        sum += ord(s)
    return sum % size

def anyHash(key, size):
    return abs(hash(key)) % size
size = 8

'''
#print (a, intHash(a, size))

for k in range(20):
    s = '89'
    for k in range(9):
        d = rn.randint(0, 9)
        s += str(d)
    print (s, numberHash(d, size))
'''

s = 'Egorova'
print(s, stringHash(s, size))

print(s, anyHash(s, size))
