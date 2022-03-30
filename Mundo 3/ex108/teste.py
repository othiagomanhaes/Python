from ex108 import moeda

p = float(input('Digite o valor: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando em 10% temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo em 13%, temos {moeda.diminuir(p, 13)}')
