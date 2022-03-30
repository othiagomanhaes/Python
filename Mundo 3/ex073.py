from time import sleep
futebol = ('Atlético Mg', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
           'Bragantino', 'Fluminense', 'América Mg', 'Atlético Go', 'Santos',
           'Ceará', 'Internacional','São Paulo', 'Athlético Pr', 'Cuiabá',
           'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print('Estes são os 5 primeiros colocados do Brasileirão 2021:')
for c in range(0, 5):
    print(f'{c + 1}º - ', futebol[c])
print('='*40)
sleep(1.5)
print('Estes são os 4 últimos colocados do Brasileirão 2021:')
for c in range(16, len(futebol)):
    print(f'{c + 1}º - ', futebol[c])
print('='*40)
sleep(1.5)
print('Estes são os times do Brasileirão 2021 em ordemalfabética:')
fut = sorted(futebol)
for c in range(0, len(futebol)):
    print(f'{c+1} - ', fut[c])
print('='*40)
sleep(2)
print('O time da Chapecoense se encontra na: ')
print(futebol.index('Chapecoense') + 1,'º posição.')

