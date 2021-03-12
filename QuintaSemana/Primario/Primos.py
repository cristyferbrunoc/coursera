def maior_primo(tamanho):
    if tamanho == 2:
        return 2
    else:
        maior = 0
        nprimo = False
        for posicao in range(tamanho + 1):
            for k in range(1, posicao):
                if posicao % k == 0 and k != 1 and posicao != k:
                    nprimo = True
            if not nprimo:
                maior = posicao
            nprimo = False
        return maior


numero = int(input('DIgite o numero: '))
print(maior_primo(numero))
