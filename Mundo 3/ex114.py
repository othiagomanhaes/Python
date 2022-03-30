# Neste código, o usuário consegue verificar a conexão de um site usando comandos do python.

import urllib
import urllib.request

try:
   site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLopener:
    print('Conexão com o site Pudim indisponível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso.')
