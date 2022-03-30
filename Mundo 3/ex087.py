matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totpar = tColun = maiSeLin = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite o valor para posição [{l}, {c}]: ')))
        if len(matriz) == 1:
            maiSeLin = matriz[1][c]
        else:
            if maiSeLin < matriz[1][c]:
                maiSeLin = matriz[1][c]
        tColun += matriz[l][2]
        if matriz[l][c] % 2 == 0:
            totpar += matriz[l][c]
print(f'{"A MATRIZ GERADA FOI":=^30}')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('='*30)
print(f'A soma de todos os números pares da matriz é {totpar}.')
print(f'A soma dos valores da terceira coluna é {tColun}.')
print(f'O maior valor da segunda linha é {maiSeLin}.')
