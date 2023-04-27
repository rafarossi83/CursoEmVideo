termo = int(input('Qual o termo: '))
razao = int(input('E a Razao: '))
cont = 1

while cont < 10:
    if cont == 1:
        print(termo, end=' → ')
    cont += 1
    termo +=razao
    print(termo, end=' → ')
print('ACABOU!')