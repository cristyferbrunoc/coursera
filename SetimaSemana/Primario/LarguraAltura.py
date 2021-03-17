largura = int(input('Digite a Largura: '))
altura = int(input('Digite a Altura: '))

for linha in range(altura):
    for coluna in range(largura):
        print('#', end="")
    print()
