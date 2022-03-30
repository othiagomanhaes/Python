def terreno():
    print('Controle de Terrenos')
    print('-' * 25)
    l = float(input('Largura (m): '))
    c = float(input('Cumprimento (m): '))
    a = l * c
    print(f'A área do um terreno de {l} x {c} é de {a} m².')


input(terreno())