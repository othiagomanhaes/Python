idade = int(input('Informe tua idade: '))

if idade <= 9:
    print('Sua categoria é MIRIM!')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categotia é JÚNIOR')
elif idade == 20:
    print('Sua categoria é Sênior ')
else:
    print('Sua categoria é MASTER')