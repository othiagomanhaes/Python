from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
x = 0
sleep(1)
while x != 5:
    x = int(input("""O que você deseja fazer com os números? \n
    [1] Somar
    [2] Multiplicar
    [3] Maior 
    [4] Novos números
    [5] Sair do programa
    Sua opção: """))
    print('-='*90)

    if x == 1:
        s = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {s}.')
    elif x == 2:
        m = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é igual a {m}.')
    elif x == 3:
        if n1 > n2:
            print(f'O número {n1} é maior do que {n2}.')
        else:
            print(f'O número {n2} é maior do que {n1}.')
    elif x == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))