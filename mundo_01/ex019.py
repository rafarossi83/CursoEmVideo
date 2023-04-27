from random import choice
aluno1 = input('Digite o nome do Aluno 1: ')
aluno2 = input('Digite o nome do Aluno 2: ')
aluno3 = input('Digite o nome do Aluno 3: ')
aluno4 = input('Digite o nome do Aluno 4: ')

sorteados = [aluno1, aluno2, aluno3, aluno4]

print('O aluno escolhido foi: {}'.format(choice(sorteados)))

