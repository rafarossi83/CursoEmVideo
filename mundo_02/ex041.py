idadeAtleta = int(input('Digite a idade do Atleta: '))

if idadeAtleta <= 9:
    print('Categoria do Atleta: MIRIM')
elif idadeAtleta <= 14:
    print('Categoria do Atleta: INFANTIL')
elif idadeAtleta <= 19:
    print('Categoria do Atleta: JUNIOR')
elif idadeAtleta == 20:
    print('Categoria do Atleta: SENIOR')
else:
    print('Categoria do Atleta: MASTER')