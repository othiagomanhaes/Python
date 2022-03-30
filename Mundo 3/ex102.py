def fatorial(num=1, show=False):
    """
    O fatorial calcula o fatorial de um número.
    :param num: O número a ser calculado
    :param show: É opcional, serve para mostrar ou não o cálculo.
    :return: O valor do fatorial de um número num
    """
    num2 = num
    m = 1
    while num > 0:
        m *= num
        num -= 1
    if show == False:
        return m
    else:
        for n in range(num2, 0, -1):
            print(f'{n} ', end='')
            if n > 1:
                print('x ', end='')
            else:
                print('= ', end='')
        return m


print(fatorial(2, True))
help(fatorial)