print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)
n = int(input('Quantos termos da sequência você quer ver? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} » {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' »  {t3}', end='')
    cont+= 1
    t1 = t2
    t2 = t3
print(' FIM')
