from random import randint
from time import sleep
from operator import itemgetter
jogador = {}
ranking = []
jogada = []
print('Valores sorteados:')
for c in range(1, 5):
    jogador[f'jogador{c}'] = randint(1, 6)
for k, v in jogador.items():
    sleep(1)
    print(f'    O {k} tirou {v}')
print()
sleep(1)
print('Ranking dos Jogadores:')
cont = 1
#Key=itemgetter serve para por em ordem um dicionário.
for k, v in sorted(jogador.items(), key=itemgetter(1), reverse=True):
    sleep(1)
    print(f'    {cont}º lugar: {k} com {v}')
    cont += 1
