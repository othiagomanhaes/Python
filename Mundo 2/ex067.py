print('-='*10)
print('PROGRAMA DA TABUADA')
print('-='*10)

while True:
    try:
        n = int(input('Você deseja saber a tabuda de qual número? '))
        if n < 0:
            break
        c = 1
        while True:
            print(f'{n} x {c} = {n*c}')
            c += 1
            if c == 10:
                break
    except:
        print('Valor digitado inválido! Tente Novamente.')
print('Fim do Programa Tabuada! Volte sempre!')