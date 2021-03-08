from math import sqrt

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o Segundo número: '))
c = int(input('Digite o Terceiro número: '))

delta = (b ** 2) - (4 * a * c)
if delta < 0:
    print('esta equação não possui raízes reais')
else:
    if delta == 0:
        print('a raiz desta equação é {}'.format(int((-b + sqrt(delta)) / (2 * a))))
    else:
        x1 = int((-b + sqrt(delta)) / (2 * a))
        x2 = int((-b - sqrt(delta)) / (2 * a))
        if (x1 < x2):
            print('as raízes da equação são {} e {}'.format(x1, x2))
        else:
            print('as raízes da equação são {} e {}'.format(x2, x1))
