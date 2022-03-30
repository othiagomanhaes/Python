pess = {}
cadastro = []
tot = 0
mulher = []
velhos = []
while True:
    pess['nome'] = str(input('Nome: '))
    while True:
        pess['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
        if pess['sexo'] in 'MF':
            break
        else:
            print('Erro! O sistema só aceita os valores "m" ou "f".')
    pess['idade'] = int(input('Idade: '))
    cadastro.append(pess.copy())
    pess.clear()
    while True:
        resp = input('Deseja continuar? [S/N]: ').strip().lower()
        if resp in 'sn':
            break
    if resp == 'n':
        break
print()
print(f'A) Foram cadastradas {len(cadastro)} pessoas.')

for i in range(0, len(cadastro)):
    tot += cadastro[i]['idade']
media = tot / len(cadastro)
print(f'B) A média de idade do grupo é de {media:.2f} anos.')

for m in range(0, len(cadastro)):
    woman = cadastro[m]['sexo']
    if woman == 'F':
        mulher.append(cadastro[m]['nome'])
print(f'C) Essa é uma lista com todas as mulheres: {mulher}.')

for a in range(0, len(cadastro)):
    old = cadastro[a]['idade']
    if old > media:
        velhos.append(cadastro[a])
print(f'D) Essa é a lista dos que tem idade a cima da média: \n{velhos}.')
