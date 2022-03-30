comida = ('Salada', 'Arroz a piamontese', 'Feijao',
          'Lasanha', 'Pizza', 'Hot-Dog', 'Uva')
print('~'*35)
print(f'{"AS VOGAIS DAS PALAVRAS":^35}')
print('~'*35)
for c in range(0, len(comida)):
    print(f'\nNa palavra {comida[c].upper()} temos ', end='')
    for d in range(0, len(comida[c])):
        if 'a' in comida[c][d].lower():
            print('a ', end='')
        if 'e' in comida[c][d].lower():
            print('e ', end='')
        if 'i' in comida[c][d].lower():
            print('i ', end='')
        if 'o' in comida[c][d].lower():
            print('o ', end='')
        if 'u' in comida[c][d].lower():
            print('u ', end='')
