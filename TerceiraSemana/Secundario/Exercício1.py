from math import sqrt

x1 = int(input('Digite x1: '))
y1 = int(input('Digite y1: '))
x2 = int(input('Digite x2: '))
y2 = int(input('Digite y2: '))

distancia = sqrt((pow(x1 - x2, 2)) + (pow(y1 - y2, 2)))
if distancia >= 10:
    print('longe')
else:
    print('perto')