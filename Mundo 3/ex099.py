from time import sleep
def maior(*num):
    print('Analisando os valores...')
    sleep(1)
    if len(num) == 0:
        print(f'Foram informados 0 valores ao todo.')
        print(f'O maior valor foi 0')
    else:
        for n in num:
            print(f'{n} ', end='', flush=True)
            sleep(0.5)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor foi {max(num)}')
        print('=-'*40)


maior(3, 4, 5, 6, 8, 14)
maior(2)
maior()
