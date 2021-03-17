largura = int(input('Digite a Largura: '))
altura = int(input('Digite a Altura: '))
for linha in range(altura):
    if linha == 0 or linha == altura - 1:
        print('{:#^{}}'.format("", largura))
    else:
        print('#{:^{}}#'.format(" ", largura - 2))
