from random import randint
from time import sleep
comp = randint(0, 5)
player = int(input('Adivinhe o número que eu pensei entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if comp == player:
    print('Acertou, Miserávi!!')
else:
    print('ERRRROOOOU!!')
sleep(0.5)
print('Eu pensei no número {} e você escolheu {}'.format(comp, player))









