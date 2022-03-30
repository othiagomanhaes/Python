ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    med = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], med])
    while True:
        resp = input('Deseja continuar: [S/N]: ').lower().strip()[0]
        if resp in 'sn':
            break
    if resp == 'n':
        break
print('-='*30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostra notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são [{ficha[opc][1]}].')
print('<<VOLTE SEMPRE!>>')
