frase = str(input('Digite uma frase: ')).strip().lower()
print('Existem {} letras a na frase.'.format(frase.count('a')))
print('Ela aparece pela primeira vez na posição {} da stringe.'.format(frase.find('a')+1))
print('Ela aparece pela ultima vez na posição {}.' .format(frase.rfind('a')+1))






