soma = 0

for i in range(0, 501, 3):
    if i % 2 != 0:
        soma += i
print('A soma dos numeros impares multiplos de 3 no intervalo de 0 a 500 e: {}'.format(soma)) 