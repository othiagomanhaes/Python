n = int(input('Digite um número: '))
s = 0
for x in range(1, n+1):
    if n % x == 0:
        s = s + 1
if s == 2:
    print('O número {} é primo.'.format(n))
elif s > 2:
    print('O número {} não é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))
