from random import randint
npc = randint(0, 4)
from time import sleep
p = 0
tot = 0
while p != npc:
    npc = randint(0, 4)
    p = int(input('Adivinhe um número entre 0 a 4.\n Seu palpite: '))
    print('Loading...')
    sleep(1)
    if p == npc:
        print('Acertou. Parabéns!')
        sleep(0.5)
        print('O NPC pensou em {} e você em {}.'.format(npc, p))
        sleep(1.5)
    else:
        print('Errooou! Tenta de novo!')
        print('-' * 85)
        sleep(0.5)
        print('O NPC pensou em {} e você em {}.'.format(npc, p))
        sleep(1.5)
    tot += 1
sleep(0.75)
print('-'*85)
print('Você precisou de {} tentativas para acertar o número.'.format(tot))