numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    while True:
        resp = input('Deseja continuar? [N/S] ').lower().strip()[0]
        if resp == 'n' or resp == 's':
            break
    if resp == 'n':
        break
print('-='*25)
print(f'Você digitou {len(numeros)} números.')
numeros.sort(reverse=True)
print(f'Os valores em ordem descrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte desta lista.')
else:
    print(f'O valor 5 não faz parte desta lista.')
