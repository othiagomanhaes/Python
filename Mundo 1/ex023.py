num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Centena: {}'.format(d))
print('Dezena: {}'.format(c))
print('Milhar: {}'.format(m))




