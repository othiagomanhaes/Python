aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input('Média do aluno: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 6.9 >= aluno['média'] >= 6:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, i in aluno.items():
    print(f'O {k} é igual a {i}')
