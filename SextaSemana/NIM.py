def computador_escolhe_jogada(n, m):
    if n - m != (n + 1):
        pass


def usuario_escolhe_jogada(n, m):
    pass


def decidir(lista):
    return True if (lista[1] + 1) % lista[0] == 0 else False


def entrada():
    quantidadeP = int(input('Digite a quantidade de Peças: '))
    limiteRetirada = int(input('Digite o limite de Retirada Peças: '))
    return [quantidadeP, limiteRetirada]


def quemComeca(teste):
    if teste:
        print('Você começa!')
    else:
        print('Computador Começa!')


def partidadaIsolada():
    escolha = entrada()
    quemComeca(decidir(escolha))
    if decidir(escolha):
        while True:
            subtrair = int(input('Digite a quantidade a ser Subtraida: '))
            if subtrair > escolha[1] or subtrair <= 0:
                print('Oops! Jogada inválida! Tente de novo.')
            else:
                usuario_escolhe_jogada(escolha[0], escolha[1])

    else:
        pass


def partidadaCampeonato():
    pass


while True:
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato')
    print('0 - Para Sair')
    escolha = int(input('Escolha: '))

    if escolha == 1:
        partidadaIsolada()
    elif escolha == 2:
        partidadaCampeonato()
    elif escolha == 0:
        break
    else:
        print('Não existe essa opção.')
