from random import randint
numeroPensado = randint(0, 5)

print(numeroPensado)
numeroUsuario = int(input('Escolha um numero de 0 a 5: '))
if numeroUsuario == numeroPensado:
    print('PARABÉNS, você acertou! Eu pensei no {}'.format(numeroUsuario))
else:
    print('QUE PENA, você errou! Eu pensei no {}'.format(numeroPensado))

