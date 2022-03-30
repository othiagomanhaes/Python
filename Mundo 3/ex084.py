lista = []
pessoa = []
maisp = []
menosp = []
totpess: int = 0
while True:
    totpess += 1
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if totpess == 1:
        maisp.append(pessoa[:])
        menosp.append(pessoa[:])
    else:
        if pessoa[1] < menosp[0][1]:
            menosp.clear()
            menosp.append(pessoa[:])
        elif pessoa[1] == menosp[0][1]:
            menosp.append(pessoa[:])

        if pessoa[1] > maisp[0][1]:
            maisp.clear()
            maisp.append(pessoa[:])
        elif pessoa[1] == maisp[0][1]:
            maisp.append(pessoa[:])
    lista.append(pessoa[:])
    pessoa.clear()
    while True:
        resp = input('Quer continuar? [S/N] ').lower().strip()[0]
        if resp in 'sn':
            break
    if resp == 'n':
        break
print('-='*35)
print(f'Foram cadastradas {totpess} pessoas.')
print(f'O maior peso cadastrado foi de {maisp[0][1]}Kg. Peso de ', end='')
for c in range(0, len(maisp)):
    print(f'[{maisp[c][0]}] ', end='')

print(f'\nO menor peso cadastrado foi de: {menosp[0][1]}Kg. Peso de ', end='')
for c in range(0, len(menosp)):
    print(f'[{menosp[c][0]}] ', end='')
