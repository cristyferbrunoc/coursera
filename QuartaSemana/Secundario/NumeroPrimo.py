numero = int(input('Digite um numero Inteiro: '))
if numero == 2:
    print('primo')
else:
    p = ''
    i = 2
    while i < numero:
        if numero % i == 0:
            p = 'não primo'
            break
        i += 1

    if p == 'não primo':
        print('não primo')
    else:
        print('primo')
