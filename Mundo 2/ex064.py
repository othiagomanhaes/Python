num = total = c = 0
while num != 999:
    num = int(input('Digite um número qualquer [999 para]: '))
    if num != 999:
        c = c + 1
        total = total + num
print(f'Foram digitados {c} números e a soma entre eles é {total}.')
