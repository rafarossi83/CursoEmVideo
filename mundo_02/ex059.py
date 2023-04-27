from time import sleep

opcao = ''
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

while opcao != 5:
    print('=-' * 20)
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Qual o Maior\n[ 4 ] Novos Numeros\n[ 5 ] Sair do Programa')
    opcao = int(input('Qual operacao deseja fazer: '))
    print('=-' * 20)

    if opcao == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('{} X {} = {}'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('O maior numero e {}'.format(num1))
        elif num2 > num1:
            print('O maior numero e {}'.format(num2))
        else:
            print('Os dois numeros sao iguais')
    elif opcao == 4:
        num1 = float(input('Digite o primeiro numero: '))
        num2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opcao Invalida, tente novamente!')

print('Programa encerrado com sucesso!')