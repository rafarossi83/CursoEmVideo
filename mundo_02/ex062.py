termo = ''
razao = ''
cont = 1
limite = 10

termo = int(input('Qual o termo: '))
razao = int(input('Qual a razao: '))

while limite != 0:
    while cont < limite:
        if cont == 1:
            print(termo, end='→')
        cont += 1
        termo += razao
        print(termo, end='→')
    print('ACABOU!')
    perg = int(input('Mais quantos termos vc quer agora (0 encerra o programa):'))
    if perg != 0:
        limite += perg
    else:
        limite = 0
print('Programa encerrado com sucesso!')
