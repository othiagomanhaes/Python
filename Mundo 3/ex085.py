par = []
impar = []
numeros = []
for c in range(1, 8):
    num = int(input('Digite o um número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
numeros.append(sorted(par))
numeros.append(sorted(impar))
print(f'Os números pares digitados foram: {numeros[0]}')
print(f'Os números ímpares digitados foram {numeros[1]}.')
