from time import sleep
from random import randint
mega = []
print('-'*30)
print(f'{"PALPITES DA MEGA SENA":^30}')
print('-'*30)
jogos = int(input('Quantos jogos você quer? '))
print(f'-='*3, f'Sorteando {jogos} jogos', '-='*3)
for c in range(1, jogos+1):
    sleep(1.2)
    while True:
        palpite = randint(1, 60)
        if palpite not in mega:
            mega.append(palpite)
        if len(mega) == 6:
            break
    print(f'Jogo {c}: {sorted(mega)}')
    mega.clear()
print(f'{" <Boa Sorte!> ":=^33}')
