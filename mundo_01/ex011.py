al = float(input('Digite a altura: '))
lg = float(input('Digite a largura: '))

ar = lg * al

print('Sua parede tem a dimensão de {}x{} e sua área é {}m².'.format(lg, al, ar))
print('Serão necessarios {} litros de tinta.'.format(ar / 2))