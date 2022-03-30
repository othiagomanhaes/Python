s = 'LISTAGEM DE PREÇO'
print('-'*45)
print(f'{s:^45}')
print('-'*45)

itens = ('Notebook', 3500, 'Mouse', 250, 'Cadeira Gamer', 2000,
         'Mesa Office', 800, 'Celular', 4000, 'Console', 4000, 'HeadSet', 270)
for c in range(0, len(itens), 2):
    print(f'{itens[c]:.<34} ', end='')
    print(f'R$ {itens[c+1]:>7.2f}')
print('-'*45)
