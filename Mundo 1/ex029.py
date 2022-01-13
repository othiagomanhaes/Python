vel = int(input('Qual foi a velocidade do carro? '))
if vel > 80:
    print('Seu carro está acima da velocidade permitida que é 80km/h!!')
    multa = (vel - 80) * 7
    print('Você será multado em R${} reais'.format(multa))
print('Boa viagem!')
