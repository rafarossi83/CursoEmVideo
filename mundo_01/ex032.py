ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    print('O ano {} É BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))