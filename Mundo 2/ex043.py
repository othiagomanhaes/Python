altura = float(input('Digite sua altura: '))
peso = int(input('Digite seu peso: '))

imc = peso / (altura * altura)
print('Seu IMC é {:.2f}.'.format(imc))

if imc < 18.5:
    print('Você está a baixo do peso.')
elif (imc >= 18.5) and (imc <= 25):
    print('Você está no peso ideial.')
elif (imc > 25) and (imc <= 30):
    print('Você está com sobrepeso.')
elif (imc > 30) and (imc <= 40):
    print('Você está obeso.')
elif imc > 40:
    print('Você está com obesidade mórbida.')