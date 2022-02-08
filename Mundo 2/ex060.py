#Algorítimo para fazer o cálculo fatorial de um número.

n = int(input('Digite um número e descubra o seu fatorial: '))

#três variáveis usados no laço que foram iniciadas em 0 (zero) para funcionar sem dar bug.
l = 0
p = 0
t = 0

"""Esse cálcuclo é feito fora do laço para pegar o próprio número e o antecessor, 
isso só ocorre uma vez. Ex: n=8, 8 x 7 = 56"""
m = n * (n-1)

"""O laço foi iniciado com n-2 no passo inicial porque já utilizamos o número e o seu antecessor
no cálculo a cima fora do passo. E o ritmo do passo está em '-1' para contar do maior par ao menor.
Ex: 5,4,3..."""
for p in range(n - 2, 0, -1):

    """A variável 't' recebeu 'm' que é a multiplicação do número e seu antecessor, 
    VEZES 'p' que é o valor de 'n' menos 2. Isso porque já utilizamos esses números no cálculo fora do
     laço"""
    t = m * p

    """"A variável 'l' guardou o valor de 't' temporariamente para depois passar para 'm' 
    que vai multiplicar ali em cima."""
    l = l + t

    """A variável 'm' guarda o valor de 'l' porque 'm' vai ser utilizada novamente para proseguir
     com o cálculo fatorial."""
    m = l

    #A variál 'l' é zerada para não alterar o valor de 'm'.
    l = 0

print(f'O cálculo fatorial de {n} vale {t}.')
