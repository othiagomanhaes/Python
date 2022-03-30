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


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c +=1
    print(linha())
    opc = leiaInt('\033[33mSua opção: \033[m')
    return opc
