termo1 = int(input('Digite o primeiro termo: '))
pa = int(input('Digite a razão da progressão aritmética: '))

l = 0
t = 0

s = termo1 + pa
x = termo1 + pa * 11

while x != s:
    t = s + pa
    l = t
    s = l
    l = 0
    print(s - pa * 2, end=' ')

