from random import choice
from time import sleep

print('=-' * 25)
print('PEDRA, PAPEL OU TESOURA')
print('=-' * 20)

jogadasMaquina = ['Pedra', 'Papel', 'Tesoura']
usuario = str(input('Digite sua jogada: ')).strip().upper()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

jogada = choice(jogadasMaquina)

print('=-' * 25)
if jogada == 'Tesoura' and usuario == 'PAPEL':
    print('Minha Jogada: {}'.format(jogada))
    print('Sua Jogada: {}'.format(usuario))
    print('Eu ganhei! Papel perde pra Tesoura')
elif jogada == 'Papel' and usuario == 'PEDRA':
    print('Minha Jogada: {}'.format(jogada))
    print('Sua Jogada: {}'.format(usuario))
    print('Eu ganhei! Pedra perde pro Papel')
elif jogada == 'Pedra' and usuario == 'TESOURA':
    print('Minha Jogada: {}'.format(jogada))
    print('Sua Jogada: {}'.format(usuario))
    print('Eu ganhei Tesoura perde pra Pedra')

elif usuario == 'TESOURA' and jogada == 'Papel':
    print('Minha Jogada: {}'.format(jogada))
    print('Sua Jogada: {}'.format(usuario))
    print('Voce Ganhou, Parabens! Papel perde pra Tesoura')
elif usuario == 'PAPEL' and jogada == 'Pedra':
    print('Minha Jogada: {}'.format(jogada))
    print('Sua Jogada: {}'.format(usuario))
    print('Voce Ganhou, Parabens! Pedra perde pro Papel')
elif usuario == 'PEDRA' and jogada == 'Tesoura':
    print('Minha Jogada: {}'.format(jogada))
    print('Sua Jogada: {}'.format(usuario))
    print('Voce Ganhou, Parabens Tesoura perde pra Pedra')
    
elif usuario == 'TESOURA' and jogada == 'Tesoura':
    print('Minha Jogada: {}'.format(jogada))
    print('Sua Jogada: {}'.format(usuario))
    print('EMPATE')
elif usuario == 'PAPEL' and jogada == 'Papel':
    print('Minha Jogada: {}'.format(jogada))
    print('Sua Jogada: {}'.format(usuario))
    print('EMPATE')
elif usuario == 'PEDRA' and jogada == 'Pedra':
    print('Minha Jogada: {}'.format(jogada))
    print('Sua Jogada: {}'.format(usuario))
    print('EMPATE')

else:
    print("Voce digitou algo errado! Tenta Novamente!")
print('=-' * 25)


    
