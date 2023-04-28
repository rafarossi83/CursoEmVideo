from time import sleep

print('=-' * 20)
print('CRIADOR DE TABUADA!\nDIGITE UM NUMERO NEGATIVO PRA ENCERRAR O PROGRAMA!')
print('=-' * 20)

while True:
    print('--' * 20)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('--' * 20)
    if num < 0:
        print('--' * 20)
        print('Finalizando...')
        sleep(1)
        break
    for i in range(1, 11):
        print(f'{num} X {i} = {num * i}')
print('Programa encerrado com sucesso')
print('--' * 20)