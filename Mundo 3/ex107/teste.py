from ex107 import moeda

p = float(input('Digite o valor: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'A metade de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando em 10% temos R${moeda.aumentar(p, 10)}')