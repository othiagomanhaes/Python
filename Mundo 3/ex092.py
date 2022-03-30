from datetime import date
from time import sleep
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - ano
pessoa['ctps'] = int(input('Carteira de trabalho: '))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['aposentadoria'] = date.today().year - ano + 35
print('-='*35)
sleep(1.5)
for k, v in pessoa.items():
    print(f'{k} tem valor {v}')
