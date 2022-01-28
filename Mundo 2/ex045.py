from time import sleep
from random import choice

sleep(0.5)
print('Ei, tu consegue me ganhar no Jokenpô?' )
sleep(2)
print('VEREMOS...')

lista = ['Pedra', 'Papel', 'Tesoura']
sleep(1)
player = input('Qual você prefere: Pedra, Papel ou Tesoura? ')
sleep(0.50)
npc = choice(lista)
print('O NPC escolheu {}.'.format(npc))

if (player == 'Tesoura') and (npc == 'Papel'):
    print('Parabéns, você venceu desta vez!')
elif (player == 'Tesoura') and (npc == 'Pedra'):
    print('A-HA! Tu perdeu, mané!')
elif (player == 'Tesoura') and (npc == 'Tesoura'):
    print('Droga! Empatamos!')

elif (player == 'Pedra') and (npc == 'Tesoura'):
    print('Parabéns, você venceu desta vez!')
elif (player == 'Pedra') and (npc == 'Papel'):
    print('A-HA! Tu perdeu, mané!')
elif (player == 'Pedra') and (npc == 'Pedra'):
    print('Droga! Empatamos!')

elif (player == 'Papel') and (npc == 'Pedra'):
    print('Parabéns, você venceu desta vez!')
elif (player == 'Papel') and (npc == 'Tesoura'):
    print('A-HA! Tu perdeu, mané!')
elif (player == 'Papel') and (npc == 'Papel'):
    print('Droga! Empatamos!')