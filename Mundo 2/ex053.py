f = str(input('Entre com a frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso +junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Não temos um palíndrmo.')