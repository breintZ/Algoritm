import math
h = 0.1
x = 0

while (x <= 3.0):
    y = (1 + math.log(x ** 2 +1))**(1/3)
    print('%.2f' % x, '%.3f' % y)
    x += h
    
    
