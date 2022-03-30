from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
        randint(1, 10), randint(1, 10))

print('-='*15)
print('  NÚMEROS ALEATÓRIOS NA TUPLA')
print('-='*15)
print(f'Esses são os números da tupla: {num}')

print(f'O {max(num)} é o maior valor da Tupla e {min(num)} é o menor valor da Tupla.')
