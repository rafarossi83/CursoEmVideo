sexo = str(input('Qual seu sexo? [M / F]: ')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual seu sexo? [M / F]: ')).upper()
    print('Voce digitou algo errado de M ou F, tente novamente...')
    
if sexo == 'M':
    print('Entendi! Voce e um Homem!')
else:
    print('Entendi! Voce e uma Mulher!')