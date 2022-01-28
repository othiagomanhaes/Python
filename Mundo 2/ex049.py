tab = int(input('Você quer saber a tabuada de qual número? '))
print('Esta é a tabuada de {}:'.format(tab))
for n in range(1, 11):
    print('{} x {} = {}'.format(tab, n, (tab * n)))
