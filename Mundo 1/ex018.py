from math import sin, cos, tan, radians
ang = float(input('Digite o valor do ângulo: '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print('O ângulo de {} \ntem O Seno valendo {:.2f},\nO Cosseno valendo {:.2f},\nE a Tangente valendo {:.2f}.'.format(ang, s, c, t))
