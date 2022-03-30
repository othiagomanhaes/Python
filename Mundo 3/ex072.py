numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezoito', 'dezenove',
           'vinte')
while True:
    while True:
        num = int(input('Qual número você quer ver por extenso? [Entre 0 a 20]: '))
        if num not in range(0, 21):
            print('Opção inválida. Tente novamente.')
        if num in range(0, 21):
            break
    print(f'O número digitado foi {numeros[num]}')
    keep = ''
    while 's' != keep != 'n':
        keep = input('Deseja continuar? [S/N]: ').lower().strip()[0]
    if keep == 'n':
        break