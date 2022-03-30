jogador = {}
gols = []
time = []
while True:
    jogador['nome'] = str(input('Qual o nome do jogador? '))
    jogador['partida'] = int(input('Quantas partidas ele jogou? '))
    for g in range(1, jogador['partida']+1):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {g}? ')))
    print('-'*45)
    jogador['gols'] = gols[:]
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).lower().strip()
        if resp in 'sn':
            break
    if resp == 'n':
        break
print('-='*45)
print(f'{"Cod":<4} {"Nome":<9} {"Gols":<9} {"Total":>10}')
print('-'*40)
c = 0
totgol = 0
for j in range(0, len(time)):
    print(f'{c:<4} {time[j]["nome"]:<8} {time[j]["gols"]}', end='')
    for goles in time[j]['gols']:
        totgol += goles
    print(f'{totgol:^10}')
    totgol = 0
    c += 1
print('-'*40)

while True:
    cod = int(input('Mostrar dados de qual jogador? [999 finaliza]: '))
    if cod == 999:
        break
    print(f'--LEVANTAMENTO DO JOGADOR {time[cod]["nome"]}')
    cont = 0
    for p in time[cod]['gols']:
        cont += 1
        print(f'Na partida {cont} fez {p} gols.')
    print('-'*40)
