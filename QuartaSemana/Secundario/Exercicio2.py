import sys


def nome() -> int:
    return 'z'

numero = input('Digite um Numero: ')
guarda = int(-1)
teste = False
for indece, c in enumerate(numero):
    if int(guarda) == int(c):
        teste = True
        break
    guarda = c
if teste:
    print('sim')
else:
    print('não')


print(nome())