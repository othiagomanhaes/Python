from time import sleep
from sys import stdout
def contador(i, f, p):
    if i > f:
        if p == 0:
            p = -1
        elif p > 0:
            p = p * -1
        print(f'Contagem de {i} até {f} no passo {p}')
        for num in range(i, f+p, p):
            print(f'{num}, ', end='')
            stdout.flush()
            sleep(0.5)
        print('FIM!')
        print('=' * 40)
    else:
        if p == 0:
            p = 1
        elif p < 0:
            p = p * -1
        print(f'Contagem de {i} até {f} no passo {p}')
        for num in range(i, f+p, p):
            print(f'{num}, ', end='', flush=True)
            sleep(0.5)
        print('FIM!')
        print('=' * 40)


contador(1, 10, 1)
contador(20, 2, -2)
print('Agora é sua vez de personalizar a contagem:')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('='*40)
contador(i, f, p)
