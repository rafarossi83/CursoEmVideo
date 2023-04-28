somador = 0
produtoMaior = 0
menorValor = 0
produtoMenor = ''

print('-' * 30)
print('LOJA SUPER BARATO')
print('-' * 30)

while True:
    produto = str(input('Nome do Produto: '))
    valor = float(input('Valor: R$'))

    if somador == 0:
        menorValor = valor
        produtoMenor = produto

    somador += valor

    if valor > 1000:
        produtoMaior += 1

    if valor < menorValor:
        produtoMenor = produto
        menorValor = valor

    cont = str(input('Quer Continuar [S/N]: '))
    while cont not in 'SsNn':
        cont = str(input('Quer Continuar [S/N]: '))

    if cont in 'Nn':
        break   

print('-----FIM DO PROGRAMA-----')
print(f'O total da compra foi {somador:.2f}')
print(f'Temos {produtoMaior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produtoMenor} que custa R${menorValor:.2f}')