pessoasMaior = 0
homens = 0
mulheresMenor = 0

while True:
    sexo = ''
    cont = ''

    print('--' * 20)
    print('CADASTRE UMA PESSOA')
    print('--' * 20)

    idade = int(input('Idade: '))

    if idade >= 18:
        pessoasMaior += 1
    
    sexo = str(input('Sexo [M/F]: '))
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: '))

    if sexo in 'Mm':
        homens += 1
    
    if sexo in 'Ff' and idade < 20:
        mulheresMenor += 1

    print('--' * 20)
    cont = str(input('Quer continuar? [S/N]: '))
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N]: '))
    
    if cont in 'Nn':
        break

print('-----FIM DO PROGRAMA-----')
print(f'Total de pessoa com mais de 18 anos: {pessoasMaior}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheresMenor} mulheres com menos de 20 anos')