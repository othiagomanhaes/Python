atacante = dict()
partidas = []
atacante['jogador'] = str(input('Qual o nome do jogador? '))
atacante['jogos'] = int(input(f'Quantas partidas {atacante["jogador"]} jogou? '))
for c in range(1, atacante['jogos']+1):
    partidas.append(int(input(f'Quantos gols na {c}ª partida? ')))
atacante['gols'] = partidas

atacante['total'] = sum(partidas)
print('=-' * 45)
print(atacante)
print('=-' * 45)
for k, v in atacante.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 45)
print(f'O jogador {atacante["jogador"]} jogou {atacante["jogos"]} partidas.')
cont = 0
for p in atacante['gols']:
    cont += 1
    print(f'    => Na partida {cont}, fez {p} gols.')
print(f'Foi um total de {atacante["total"]} gols.')
