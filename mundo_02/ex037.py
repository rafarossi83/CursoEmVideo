numeroUsuario = int(input('Digite um numero: '))
escolha = int(input('1 - Binario\n2 - Octal\n3 - Hexadecimal\nEscolha uma conversao: ').strip())

if escolha == 1:
    print('{} em Binario equivale: {}'.format(numeroUsuario, bin(numeroUsuario)))
elif escolha == 2:
    print('{} em Octal equivale: {}'.format(numeroUsuario, oct(numeroUsuario)))
elif escolha == 3:
    print('{} em Hexadecimal equivale {}'.format(numeroUsuario, hex(numeroUsuario)))
else:
    print('Opcao Invalida, Tente Novamente!')