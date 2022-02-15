vontade = 1
guardanum = num = menornum = maiornum = contador = 0
siga = 's'

while siga == 's':
    num = int(input('Digite um número inteiro: '))
    guardanum = guardanum + num
    contador = contador + 1
    siga = input('Deseja seguir digitando? Digite S/N: ').lower()
    if num > maiornum:
        maiornum = num

    if contador == 1:
        menornum = num
    if num < menornum:
        menornum = num

media = guardanum/contador
print(f'Você digitou {contador} números e a média entre eles é {media:.2f} .')
print(f'O maior número digitado foi {maiornum} e o menor foi {menornum}.')