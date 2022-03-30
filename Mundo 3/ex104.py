def leiaInt(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            break
        else:
            print('\033[31mERRO! Digite um número inteiro!\033[m')
    return num


n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')
