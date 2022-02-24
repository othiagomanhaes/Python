print('-~'*20)
print('             CAIXA ELETRÔNICO')
print('-~'*20)
valor = int(input('Quanto deseja sacar? R$'))

if valor >= 50:
    tot50 = valor // 50
    print(f'Você receberá {tot50} notas de R$50')
    rest50 = valor % 50
    if rest50 >= 20:
        tot20 = rest50 // 20
        print(f'Você receberá {tot20} notas de R$20')
        rest20 = rest50 % 20
        if rest20 >= 10:
            tot10 = rest20 // 10
            print(f'Você receberá {tot10} notas de R$10')
            rest10 = rest20 % 10
            if rest10 >= 1:
                tot1 = rest10 // 1
                print(f'Você receberá {tot1} notas de R$1')

    elif rest50 >= 10:
        tot10 = rest50 // 10
        print(f'Você receberá {tot10} notas de R$10')
        rest10 = rest50 % 10
        if rest10 >= 1:
            tot1 = rest10 // 1
            print(f'Você receberá {tot1} notas de R$1')

    elif rest50 >= 1:
        tot1 = rest50 // 1
        print(f'Você receberá {tot1} notas de R$1')

elif valor >= 20:
    tot20 = valor // 20
    print(f'Você reveberá {tot20} notas de R$20')
    rest20 = valor % 20
    if rest20 >= 10:
        tot10 = rest20 // 10
        print(f'Você reveberá {tot10} notas de R$10')
        rest10 = rest20 % 10
        if rest10 >= 1:
            tot1 = rest10 // 1
            print(f'Você reveberá {tot1} notas de R$1')

    elif rest20 >= 1:
        tot1 = rest20 // 1
        print(f'Você reveberá {tot1} notas de R$1')

elif valor >= 10:
    tot10 = valor // 10
    print(f'Você receberá {tot10} notas de R$10')
    rest10 = valor % 10
    if rest10 >= 1:
        tot1 = rest10 // 1
        print(f'Você receberá {tot1} notas de R$1')
elif valor >= 1:
    tot1 = valor // 1
    print(f'Você receberá {tot1} notas de R$1')
print('')
print('-~'*20)
print('Obrigado pela preferência! Volte sempre!')

