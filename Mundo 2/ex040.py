nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Você foi Aprovado!')
elif media >= 5 and media <= 6.9:
    print('Você está de Recuperação!')
elif media < 5:
    print('Você foi Reprovado!')