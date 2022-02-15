# Algoritmo pra calcular o fatorial de um número
num = int(input('Digite o número para saber seu Fatorial: '))
guardanum = 1
recebenum = num
soma = 0
# O laço precisa acontecer antes que o numero chegue a 0, porque senão, o valor será 0.
while num > 0:
    guardanum *= num
    num -= 1
    soma += guardanum
print(f'E o fatorial de {recebenum} é {guardanum}')