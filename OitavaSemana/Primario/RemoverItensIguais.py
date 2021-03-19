def remove_repetidos(lista):
    listaNova = []
    for numero in lista:
        if numero not in listaNova:
            listaNova.append(numero)
    return sorted(listaNova)

print(remove_repetidos([7,3,33,12,3,3,3,7,12,100]))
