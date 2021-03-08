def fatorial(n: int):
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n - 1)


numero = int(input('Digite o numero: '))
print(fatorial(numero))
