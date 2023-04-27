from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do Ângulo: '))
rad = radians(angulo)

print('Com o ângulo de {}° temos: '.format(angulo))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sin(rad), cos(rad), tan(rad)))