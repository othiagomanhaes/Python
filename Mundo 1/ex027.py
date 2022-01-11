nome = str(input('Digite o teu nome completo: ')).strip()
name = nome.split()
print('O primeiro nome é: {}'.format(name[0]))
print('O último nome é: {}'.format(name[len(name)-1]))

