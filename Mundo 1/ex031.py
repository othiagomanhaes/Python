dist = float(input('Olá, qual é a distância da tua viagem? '))
if dist <= 200:
    valor = 0.50 * dist
    print('Você irá pagar R${} reais.'.format(valor))
else:
    valor = 0.45 * dist
    print('Você irá pagar R${} reais.'.format(valor))

