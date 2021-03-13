def computador_escolhe_jogada(n, m):
    if n <= m:
        return n

    else:
        quantia = n % (m + 1)
        if quantia > 0:
            return quantia
        return m


def usuario_escolhe_jogada(n, m):
    while True:
        retirar = int(input('Quantas peças você vai tirar?'))
        if (retirar > m) or (retirar <= 0) or (retirar > n):
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            return retirar


def campeonato():
    pontos_voce = 0
    pontos_cpu = 0
    rodada = 1
    print('Voce escolheu um campeonato!')
    while rodada <= 3:
        print('**** Rodada ', rodada, ' ****')
        resultado = partida()
        if resultado == 0:
            pontos_voce += 1
        else:
            pontos_cpu += 1
            rodada = rodada + 1
    print('**** Final do campeonato! ****')
    print('Placar: Você ', pontos_voce, ' X ', pontos_cpu, ' Computador')


def partida():
    while True:
        qtd_pecas = int(input('Quantas peças?'))
        limite_pecas = int(input('Limite de peças por jogada?'))
        break

    qtd_pecas_current = qtd_pecas
    if checa_multiplos(qtd_pecas_current, limite_pecas):
        print('Voce começa!')
        user_starts = True
    else:
        print('Computador começa!')
        user_starts = False
    # GAME LOOP
    while True:
        if user_starts:
            qtd_pecas_return = usuario_escolhe_jogada(qtd_pecas_current, limite_pecas)
            print('Você tirou', qtd_pecas_return, plural(qtd_pecas_return))
            user_starts = False
        else:
            qtd_pecas_return = computador_escolhe_jogada(qtd_pecas_current, limite_pecas)
            print('O computador tirou', qtd_pecas_return, plural(qtd_pecas_return))
            user_starts = True

        qtd_pecas_current = qtd_pecas_current - qtd_pecas_return

        if qtd_pecas_current > 0:
            pass
        else:
            if not user_starts:
                print('Você ganhou!')
                return 0
            else:
                print('O computador ganhou!')
                return 1


def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')

    print('\n1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato\n')

    opt = int(input('Escolhe a partida: '))
    if opt == 1:
        partida()
    else:
        campeonato()


def plural(n):
    if (n == 1) or (n == -1):
        return 'peça.'
    else:
        return 'peças.'


def checa_multiplos(n, m):
    if n % (m + 1) == 0:
        return True
    else:
        return False


# START GAME
main()
