def fatorial(n):
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n - 1)


lista = []
for i in range(4):
    lista.append(int(input('Digite um numero: ')))

for k in lista:
    print(f'{fatorial(k)}, ', end='')
