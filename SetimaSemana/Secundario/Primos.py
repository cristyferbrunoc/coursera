def n_primos(numero):
    contagem = 1
    divisor = 2
    dividendo = 2
    primo = True
    somaPrimos = 0
    while contagem < numero:
        while divisor != dividendo:
            if dividendo % divisor == 0:
                primo = False
                break
            divisor += 1
        if primo:
            somaPrimos += 1
        contagem += 1
        primo = True
        dividendo += 1
        divisor = 2
    return somaPrimos


print(n_primos(4))
