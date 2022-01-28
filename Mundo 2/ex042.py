r1 = int(input('Digite o valor de uma reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))

if (r1 < (r2 + r3)) and (r2 < (r1 + r3)) and (r3 < (r1 + r2)):
    if r1 == r2 == r3:
        print('Seu triângulo é equilátero!')
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print('Seu triângulo é isósceles!')
    else:
        print('Seu trinângulo é escaleno!')
else:
    print('Você não consegue montar um triângulo com essas retas.')