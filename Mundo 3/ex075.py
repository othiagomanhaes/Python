num = (int(input('Digite o primeiro número: ')),
        int(input('Digite o segundo número: ')),
        int(input('Digite o terceiro número: ')),
        int(input('Digite o quarto número: ')))


print(f'Voce digitou: {num}')
print('')
print(f'O número 9 apareceu {num.count(9)} vezes.')

try:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição.')
except:
    print('Você não digitou o número 3.')

print('Os valores pares digitados foram: ', end='')
for c in range(0, 4):
    if num[c] % 2 == 0:
        print(f'{num[c]} ', end='')
