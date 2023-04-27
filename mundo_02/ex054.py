from datetime import date
anoAtual = date.today().year
maiores = 0
menores = 0

for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    if (anoAtual - ano) < 21:
        menores += 1
    else:
        maiores += 1
print('Dos anos informados {} sao menores e {} sao maiores de idade'.format(menores, maiores))


