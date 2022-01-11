from math import hypot
cat1 = float(input('Digite o cateto oposto: '))
cat2 = float(input('Digite o cateto adjacente: '))
hipo = hypot(cat1, cat2)
print('A hipotenusa tem o cumprimento de {:.2f}.'.format(hipo))



