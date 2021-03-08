def fatorial(n):
    if (n == 1 or n == 0):
        return 1
    return n * fatorial(n - 1)


n = int(input('Digite o primeiro numero: '))
k = int(input('Digite o segundo Numero: '))

print('{}'.format(fatorial(n) / (fatorial(k) * fatorial((n - k)))))
