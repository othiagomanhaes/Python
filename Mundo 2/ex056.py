somaidade = 0
medidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for pess in range(1, 5):
    print('----- {}ª-----'.format(pess))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if pess == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        totmulher += 1
medidade = somaidade / 2
print('A média de idade do grupo é de {} anos.'.format(medidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher))
