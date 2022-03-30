lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        resp = input('Deseja continuar? [N/S] ').lower().strip()[0]
        if resp in 'ns':
            break
    if resp == 'n':
        break
print('~'*30)
print(f'A lista digitada foi {lista}')
par = []
impar = []
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        n1 = lista[c]
        par.append(n1)
    else:
        n2 = lista[c]
        impar.append(n2)
print(f'A lista de números pares digitados é {par}')
print(f'A lista de números ímpares digitados é {impar}')
