def ficha(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} marcou {gols} gol(s).')


n = str(input('Jogador: '))
g = str(input('Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

