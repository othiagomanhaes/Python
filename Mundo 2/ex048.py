t = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        t = n + t
print('Esta é a soma de todos os múltiplos de 3 de 1 a 500 {}.'.format(t))

