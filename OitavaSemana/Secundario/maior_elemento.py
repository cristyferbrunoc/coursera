def maior_elemento(lista):
    maior = min(lista)
    for numero in lista:
        if numero > maior:
            maior = numero
    # Poderia Retornar somente return max(lista) sem todo esse codigo
    return maior


