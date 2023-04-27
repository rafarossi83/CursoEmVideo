numero = ''
somador = 0
numerosDigitados = []

print('=-' * 20)
print('Bem vindo ao somador de numeros!\nDigite 999 para encerrar o programa!')
print('=-' * 20)

while numero != 999:
    numero = int(input('Digite um numero aleatorio: ').strip())
    if numero != 999:
        somador += numero
        numerosDigitados.append(numero)
print('O numeros digitados foram: {}'.format(numerosDigitados))
print('E sua soma vale {}'.format(somador))