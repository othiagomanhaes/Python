num = int(input('Escolha o número a ser convertido: '))
print('''Escolha uma das bases para conversão:
[1] para base BINÁRIA.
[2] para base OCTAL
[3] para base HEXADECMAL''')
opcão = int(input('Escolha sua opção: '))

if opcão == 1:
    print('{} convertido para BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif opcão == 2:
    print('{} convertido para OCTAL é {}.'.format(num, oct(num)[2:]))
elif opcão == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
