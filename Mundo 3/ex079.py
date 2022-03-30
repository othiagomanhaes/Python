valor = []
while True:
    n = int(input('Digite um número: '))
    if n in valor:
        print('Número duplicado. Não podemos adicionar!')
    elif n not in valor:
        valor.append(n)
    while True:
        resp = input('Deseja continuar? [S/N] ').lower().split()[0]
        if resp in 'ns':
            break
    if resp == 'n':
        break
print(f'Você digitou os valores {sorted(valor)}.')
