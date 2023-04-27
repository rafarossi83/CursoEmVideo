from random import randint

tentativas = 0
numeroPensado = randint(0, 10)
jogadaUsuario = ''

print('=-' * 20)
print('Tente advinhar o numero!')
print('=-' * 20)

while jogadaUsuario != numeroPensado:
    jogadaUsuario = int(input('Qual o numero que pensei? '))
    if jogadaUsuario < numeroPensado:
        print('Mais...Tente Novamente: ')
    elif jogadaUsuario > numeroPensado:
        print('Menos...Tente Novamente: ')
    tentativas += 1
print('Parabens voce acertou o numero com {} tentativa(s)'.format(tentativas))