num = []
mai = 0
men = 0
for c in range(0, 5):
    num.append(int(input(f'Digite o valor para posição {c}: ')))
    if c == 0:
        mai = men = num[c]
    else:
        if num[c] > mai:
            mai = num[c]
        if num[c] < men:
            men = num[c]
print('=-='*20)

print(f'Você digitou os valores {num}.')
print(f'O maior valor dgitado foi {mai} na posição ', end='')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} na posição ', end='')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}...', end='')
