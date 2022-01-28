prec =  float(input('Qual é o valor do produto? '))
pag = input('Qual é a forma de pagamento? (Cartão/Cheque/Dinheiro) ')

if (pag == 'Cheque') or (pag == 'Dinheiro'):
    prec1 = prec * 0.9
    print('Você tem 10% de desconto, o novo valor é R${:.2f} reais.'.format(prec1))
elif (pag == 'Cartão'):
    cart = input('Qual modo? (à vista/parcelado) ')
    if (cart == 'à vista'):
        prec2 = prec * 0.95
        print('Você tem 5% de desconto, o novo valor é R${:.2f} reais.'.format(prec2))
    elif (cart == 'parcelado'):
        parc = input('Em quantas vezes? ')
        if parc == '2':
            print('O preço será de R${}.'.format(prec))
        elif parc > '2':
            prec3 = prec * 1.2
            print('O preço será de R${:.2f}.'.format(prec3))

