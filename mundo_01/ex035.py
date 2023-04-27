lado1 = float(input('Digite o valor de uma reta: '))
lado2 = float(input('Digite o valor de outra reta: '))
lado3 = float(input('Digite o valor de mais uma reta: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Formam Triangulo')
else:
    print('Não formam triangulo!')