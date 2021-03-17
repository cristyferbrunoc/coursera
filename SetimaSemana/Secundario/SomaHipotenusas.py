def é_hipotenusa(numeroTeste):
    for ladoA in range(1, numeroTeste ** 2):
        for ladoB in range(1, numeroTeste ** 2):
            if numeroTeste ** 2 == ladoA ** 2 + ladoB ** 2:
                return True
            if ladoB ** 2 + ladoA ** 2 > numeroTeste ** 2:
                break
    return False


def soma_hipotenusas(comprimento):
    soma = 0
    for i in range(1, comprimento + 1):
        if é_hipotenusa(i):
            soma += i
    return soma


print(soma_hipotenusas(121))
