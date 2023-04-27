valorOriginal = float(input('Digite o valor do produto: '))

desconto = valorOriginal * 5 / 100
valorDesconto = valorOriginal - desconto

print('O produto de {} com 5% de desconto agora custa {}'.format(valorOriginal, valorDesconto))