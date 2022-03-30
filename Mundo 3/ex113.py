def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro! Você não digitou um número inteiro.\033[m')
        except KeyboardInterrupt:
            print('\033[31mErro! Você não entrou com dados pelo teclado.\033[m')
        except Exception as erro:
            print(f'\033[31mErro! Sua declaração tem um erro de ({erro})\033[m')
        else:
            if True:
                return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro! Você não digitou um número real.\033[m')
        except KeyboardInterrupt:
            print('\033[31mErro! Você não entrou com dados no teclado!\033[m')
        except Exception as erro:
            print(f'\033[31mErro! Você cometeu um erro de ({erro})\033[m')
        else:
            if True:
                return num


i = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {i} e o real foi {f}.')
