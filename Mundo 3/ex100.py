from random import randint
from time import sleep
num = []
def sorteia():
    print('Sorteando 5 valores: ', end='')
    for c in range(0, 5):
        valor = randint(1, 10)
        num.append(valor)
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        valor = 0
    print('PRONTO!')

def somaPar():
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {num} temos: {soma}')


sorteia()
somaPar()
