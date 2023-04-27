nome = input('Digite o nome do Aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda: '))

md = (n1 + n2) / 2

print('=-' * 20)
print('Média do {}'.format(nome))
print('=-' * 20)

print('Nota 01: {}\nNota 02: {}\nMédia: {}'.format(n1, n2, md))