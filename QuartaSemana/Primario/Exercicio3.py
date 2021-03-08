numero = int(input('Digite o numero: '))
i = int(0)
soma = int(0)
tamanho = len(str(numero))
while i < tamanho:
    soma += numero % 10
    numero = numero // 10
    i += 1
print(soma)
