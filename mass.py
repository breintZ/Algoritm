import random
from random import randint
n = 10
mas = [randint(1,100) for i in range(n)]
 
MaxEl = mas[0]
for i in range(1,n):
                if mas[i] > MaxEl:
                               MaxEl  = mas[i]
print ('max = ',MaxEl, 'massive = ', *mas)
