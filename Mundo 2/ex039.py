from datetime import date
atual = date.today().year
ano = int(input('Olá, informe o ano em que você nasceu: '))

if atual - ano > 18:
    tempo = 2021 - ano - 18
    print('Meu jovem, você está atrasado {} ano(s).'.format(tempo))
elif atual - ano < 18:
    tempo1 = ano - 2021 + 18
    print('Olá, amigo, ainda faltam {} ano(s) para seu alistamento.'.format(tempo1))
else:
   print('Olá, seja bem vindo. Você chegou no tempo certo.')