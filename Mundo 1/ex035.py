r1 = int(input('Digite o valor de uma reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))

if (r1 < (r2 + r3)) and (r2 < (r1 + r3)) and (r3 < (r1 + r2)) :
    print('Você pode montar um triângulo com essas retas.')
else:
    print('Você não pode montar um triângulo come essas retas.')