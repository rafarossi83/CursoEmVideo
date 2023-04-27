n1 = float(input('Digite a Nota 01: '))
n2 = float(input('Digite a Nota 02: '))

media = (n1 + n2) / 2

if media < 5:
    print('ALUNO \033[31m'+'REPROVADO'+'\033[0;0m')
    print('Media: {}'.format(media))
elif media > 5 and media < 6.9:
    print('ALUNO \033[33mDE RECUPERACAO\033[0m')
    print('Media: {}'.format(media))
else:
    print('ALUNO \033[32m'+'APROVADO'+'\033[0;0m')
    print('Media: {}'.format(media))