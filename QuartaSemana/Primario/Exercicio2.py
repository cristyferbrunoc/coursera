numero = int(input('Digite o número: '))

i = 1
impar = 1
while i <= numero:
    while True:
        teste = impar % 2
        if (teste != 0):
            print(impar)
            break
        else:
            impar += 1
    impar += 1
    i += 1
