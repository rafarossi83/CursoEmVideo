print('=-' * 20)
print('Calculo de Tabuada')
print('=-' * 20)

numero = int(input('Digite o numero da Tabuada: '))
for i in range(1, 11):
    print('{} X {} = {}'.format(numero, i, numero * i))