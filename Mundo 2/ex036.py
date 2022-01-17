nome = str(input('Informe o teu nome: '))
casa = float(input('Olá, {}. Qual o valor da casa? '.format(nome)))
salario = float(input('Qual é o teu salário mensal, {}? '.format(nome)))
tempo = float(input('Em quantos anos pretende pagar? '))

prestacao = casa / (tempo * 12)

if prestacao > salario * 0.30:
    print('Desculpe-nos, {}. Nós não podemos lhe conceder um empréstimo.'.format(nome))
    print('A prestação está no valor de R${:.2f}.'.format(prestacao))
else:
    print('Será um prazer em lhe conceder este empréstimo, {}.'.format(nome))