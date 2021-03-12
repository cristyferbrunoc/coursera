def computador_escolhe_jogada(n, m):
    soma = (m + 1)
    if n - m != soma:
        return (n - (soma + 1)) - m


n = 20
m = 8
n -= computador_escolhe_jogada(n, m)
n -= 2
print(n)