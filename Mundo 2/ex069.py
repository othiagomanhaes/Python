quantidade = conthom = contmul = 0
while True:
    print('------CADASTRO DE PESSOAS------')
    while True:
        #try/except para caso a pessoa digite algo que não seja algorismo, o algoritmo não bugar.
        try:
            idade = int(input('Idade: '))
            if idade > 18:
                quantidade += 1
            if idade != (1, 100):
                break
        except:
            print('Idade inválida. Tente novamente.')

    while True:
        sexo = input('Sexo [F/M]: ')
        if sexo == 'm':
            conthom += 1
        if sexo == 'm' or sexo == 'f':
            break
    if idade < 20 and sexo == 'f':
        contmul += 1
    #enquanto o usuário não digitar 's' ou 'n', a pergunta de continuar ou não se repete.
    while True:
        progra = input('Quer continuar? [N/S]').lower().strip()[0]
        if progra in 'sn':
            break
    #quebra o loop(while) de cadastrar pessoas.
    if progra == 'n':
        break
print('')
print(f"""O programda detectou {quantidade} maiores de 18 anos.
E foram cadastrados {conthom} homens.
Também cadastramos {contmul} mulheres com menos de 20 anos.""")