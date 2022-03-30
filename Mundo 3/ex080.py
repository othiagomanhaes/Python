numeros = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0:
        numeros.insert(0, num)
        print('Adicionado no final da lista.')

    if c == 1:
        if num > numeros[0]:
            numeros.append(num)
            print('Adicionado no final da lista.')
        else:
            numeros.insert(0, num)
            print('Adicionado na posição 0 da lista.')

    if c == 2:
        if num > numeros[1]:
            numeros.append(num)
            print('Adicionado no final da lista.')
        elif num > numeros[0]:
            numeros.insert(1, num)
            print('Adicionado na posição 1 da lista.')
        elif num < numeros[0]:
            numeros.insert(0, num)
            print('Adicionado na posição 0 da lista.')

    if c == 3:
        if num > numeros[2]:
            numeros.append(num)
            print('Adicionado no final da lista.')
        elif num > numeros[1]:
            numeros.insert(2, num)
            print('Adicionado na posição 2 da lista.')
        elif num > numeros[0]:
            numeros.insert(1, num)
            print('Adicionado na posição 1 da lista.')
        elif num < numeros[0]:
            numeros.insert(0, num)
            print('Adicionado na posição 0 da lista.')

    if c == 4:
        if num > numeros[3]:
            numeros.append(num)
            print('Adicionado no final da lista.')
        elif num > numeros[2]:
            numeros.insert(3, num)
            print('Adicionado na posição 3 da lista.')
        elif num > numeros[1]:
            numeros.insert(2, num)
            print('Adicionado na posição 2 da lista.')
        elif num > numeros[0]:
            numeros.insert(1, num)
            print('Adicionado na posição 1 da lista.')
        elif num < numeros[0]:
            numeros.insert(0, num)
            print('Adicionado na posição 0 da lista.')

        if c == 5:
            if num > numeros[4]:
                numeros.append(num)
                print('Adicionado no final da lista.')
            elif num > numeros[3]:
                numeros.insert(4, num)
                print('Adicionado na posição 4 da lista.')
            elif num > numeros[2]:
                numeros.insert(3, num)
                print('Adicionado na posição 3 da lista.')
            elif num > numeros[1]:
                numeros.insert(2, num)
                print('Adicionado na posição 2 da lista.')
            elif num > numeros[0]:
                numeros.insert(1, num)
                print('Adicionado na posição 1 da lista.')
            elif num < numeros[0]:
                numeros.insert(0, num)
                print('Adicionado na posição 0 da lista.')

print(numeros)

