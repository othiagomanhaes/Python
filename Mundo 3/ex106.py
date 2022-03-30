from time import sleep
def titulo(txt):
    tam = len(txt) + 4
    traço = '=' * tam
    print(f'\033[43m')
    print(traço)
    print(f'  {txt}')
    print(traço)
    print(f'\033[m')

def titulo2(txt):
    tam = len(txt) + 4
    traço = '=' * tam
    print(f'\033[44m')
    print(traço)
    print(f'  {txt}')
    print(traço)
    print(f'\033[m')

def titulo3(txt):
    tam = len(txt) + 4
    traço = '=' * tam
    print(f'\033[41m')
    print(traço)
    print(f'  {txt}')
    print(traço)
    print(f'\033[m')

def PyHelp():
    while True:
        titulo('Sistema de Ajuda PyHelp')
        sleep(1)
        ajuda = str(input('Função ou Bilbioteca > ')).lower().strip()
        if ajuda == 'fim':
            titulo3('FIM!')
            break
        titulo2(f'Analisando o Manual do {ajuda}')
        sleep(1)
        print(f'\033[40m')
        print(f'{help(ajuda)}')
        print(f'\033[m')


PyHelp()
