from ex109 import moeda

p = float(input('Digite o valor: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando em 10% temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuir em 13% temos {moeda.aumentar(p, 13, True)}')
