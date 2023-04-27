soma = 0
numeroPares = []

for i in range(0, 6):
    numero = int(input('Digite um numero: ').strip())
    if numero % 2 == 0:
        soma += numero
        numeroPares.append(numero)
        
print('O numeros Pares digitados foram: {}'.format(numeroPares), end=' ')
print('e sua soma e {}'.format(soma))

