numeros = []

while True:
    numeros.append(int(input('Digite o numero: ')))
    if numeros.count(0) == 1:
        break

numeros = list(filter(lambda i: i != 0, numeros))
revertido = numeros[::-1]

for i in revertido:
    print(i)
