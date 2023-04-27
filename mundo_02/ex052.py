numero = int (input('Digite um numero: '))
divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print('O numero {} e primo'.format(numero))
else:
    print('O numero {} nao e primo'.format(numero))
