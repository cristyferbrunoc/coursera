entrada = int(input('Por favor, entre com o número de segundos que deseja converter: '))
segundos = entrada % 60
minutos = (entrada // 60) % 60
horas = (entrada // 3600) % 24
dia = entrada // 86400

print(f'{dia} dias, {horas} horas, {minutos} minutos e {segundos} segundos.')
