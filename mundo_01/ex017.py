from math import hypot

catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o cateto adjacente: '))

print('O valor da hipotenusa é: {:.2f}'.format(hypot(catetoOposto, catetoAdjacente)))