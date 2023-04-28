from random import randint

vitorias = 0

print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)

while True:
    jogadaMaquina = randint(0, 10)
    jogadaUsuario = int(input('Diga um valor: ').strip())
    opcao = str(input('Voce quer par ou impar? [P/I]: ')).strip()

    if opcao in 'Ii':
        if (jogadaUsuario + jogadaMaquina) % 2 == 0:
            print('=-' * 20)
            print(f'Voce Jogou {jogadaUsuario} e o computador {jogadaMaquina} total: {jogadaMaquina + jogadaUsuario} deu PAR')
            print('Voce PERDEU!\nEncerrando Programa...')
            print('=-' * 20)
            break
        else:
            print('=-' * 20)
            print(f'Voce jogou {jogadaUsuario} o computador {jogadaMaquina} total: {jogadaMaquina + jogadaUsuario} deu IMPAR')
            print('Voce VENCEU\nVamos jogar novamente...')
            print('=-' * 20)
            vitorias += 1
    elif opcao in 'Pp':
        if (jogadaUsuario + jogadaMaquina) % 2 == 0:
            print('=-' * 20)
            print(f'Voce jogou {jogadaUsuario} o computador {jogadaMaquina} total: {jogadaMaquina + jogadaUsuario} deu PAR')
            print('Voce VENCEU!\nVamos jogar novamente...')
            print('=-' * 20)
            vitorias += 1
        else:
            print('=-' * 20)
            print(f'Voce jogou {jogadaUsuario} o computador {jogadaMaquina} total: {jogadaMaquina + jogadaUsuario} deu IMPAR')
            print('Voce PERDEU\nEncerrando programa!')
            print('=-' * 20)
            break
    else:
        print('=-' * 20)
        print('Opcao INVALIDA\nTente Novamente!')
        print('=-' * 20)
print(f'GAME OVER! Voce venceu {vitorias} vezes.')
