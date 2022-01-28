termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A.: '))
termo2 = termo1 + razao * 10
for n in range(termo1, termo2, razao):
    print(n, end=' ')
