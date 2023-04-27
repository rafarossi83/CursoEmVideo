soma = 0
maior = 0
contMulheres = 0

for i in range(1, 5):
    print('-------{} Pessoa -------'.format(i))
    nome = str(input('Digite o nome: ').strip())
    idade = int(input('Digite a idade: ').strip())
    sexo = str(input('Qual o genero? [F / M]: ').strip()).upper()
    soma += idade
    if sexo == 'M':
        if idade > maior:
            maior = idade
    if sexo == 'F':
        if idade < 20:
            contMulheres += 1
        

print('A media de idade do grupo e {} anos'.format(soma / 4))

if maior == 0:
    print('Nao tem nenhum homem')
else:
    print('O homem mais velho tem {} anos'.format(maior))
    
print('Existem {} mulhere(s) com menos de 20 anos'.format(contMulheres))