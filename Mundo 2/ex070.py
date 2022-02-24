print('~-'*18)
print('     CADASTRO DE PRODUTOS')
print('~-'*18)
totalpreco = maisdmil = maisBarato = 0
nomeMaisBarato = ''
while True:
    while True:
        nomep = input('Qual o nome do produto? ')
        if nomep != '':
            break
    while True:
        precop = float(input('Qual o preço do produto? R$'))
        totalpreco += precop
        if precop > 1000:
            maisdmil += 1
        if maisBarato == 0 or maisBarato > precop:
            maisBarato = precop
            nomeMaisBarato = nomep

        if precop > 0:
            break

    seguir = input('Tem mais produtos? [S/N]').strip()[0].lower()
    print('_-'*20)
    if seguir == 'n':
        break

print(f"""O total de gastos na compra foi de R${totalpreco}.
Foram comprados {maisdmil} produtos que custou acima de R$1000,00 cada.
E {nomeMaisBarato } foi o produto mais barato custando R${maisBarato}""")