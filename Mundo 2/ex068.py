import random
from time import sleep

print('~-'*18)
print('BEM-VINDO AO JOGO DO PAR OU ÍMPAR')
print('~-'*18)
c = v = 0
while True:
    sleep(1)
    print('')
    c += 1
    jogador = ''
    while (jogador != 'p') and (jogador != 'i'):
        jogador = input("""Qual você prefere:
        [P] Par
        [I] Ímpar
        Sua escolha: """).strip().lower()
        if (jogador != 'p') and (jogador != 'i'):
            print('Resposta inválida! Tente novamente.')
        print('')

    computador = random.randint(0, 10)
    sleep(0.5)
    try:
        jogescolha = int(input('Qual número você vai escolher? '))
    except:
        print('Opção inválida! Tente novamente.')

    soma = computador + jogescolha
    print('Calculando...')
    sleep(1.5)

    if soma % 2 == 0 and jogador == 'p':
        v += 1
        print('Parabéns! Você venceu.')
        print(f'O computador Jogou {computador} e você {jogescolha}.')
        print(f'Deu PAR porque a soma de {computador} e {jogescolha} é igual {soma}.')

    if soma % 2 != 0 and jogador == 'p':
        print('Você perdeu!')
        print(f'O computador Jogou {computador} e você {jogescolha}.')
        print(f'Deu ÍMPAR porque a soma de {computador} e {jogescolha} é igual {soma}.')

        break
    if soma % 2 != 0 and jogador == 'i':
        v += 1
        print('Parabéns! Você venceu.')
        print(f'O computador Jogou {computador} e você {jogescolha}.')
        print(f'Deu ÍMPAR porque a soma de {computador} e {jogescolha} é igual {soma}.')

    if soma % 2 == 0 and jogador == 'i':
        print('Você perdeu!')
        print(f'O computador Jogou {computador} e você {jogescolha}.')
        print(f'Deu PAR porque a soma de {computador} e {jogescolha} é igual {soma}.')
        break
sleep(1)
print('')
print('~-'*23)
print(f'Você jogou {c} vezes e venceu {v} vezes.')
print('~-'*23)
