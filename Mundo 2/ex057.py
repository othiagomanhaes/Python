s = ''
while 'm' != s != 'f':
    s = str(input('Informe teu sexo: ')).lower().strip()
    if s != 'f' or 'm':
        print('Dados inválidos. Tente novamente!')
print(f'Sexo {s} registrado com sucesso')


