sal = float(input('Informe o teu salário: '))
if sal > 1250:
    sal = sal + sal * 0.10
    print('Seu salário foi reajustado para R${:.2f}.'.format(sal))
if sal <= 1250:
    sal = sal + sal * 0.15
    print('Seu salário foi reajustado para R${:.2f}.'.format(sal))
