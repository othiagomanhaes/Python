for pess in range(1, 6):
    peso = input('Peso da {}º pessoa: '.format(pess))
    if pess == 1:
        p1 = peso
    elif pess == 2:
        p2 = peso
    elif pess == 3:
        p3 = peso
    elif pess == 4:
        p4 = peso
    elif pess == 5:
        p5 = peso
maior = max([p1, p2, p3, p4, p5])
menor = min([p1, p2, p3, p4, p5])
print('O maior peso foi de {}Kg.'.format(maior))
print('O menor peso foi de {}Kg.'.format(menor))





