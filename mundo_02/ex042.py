lado1 = float(input('Digite o Lado 01: '))
lado2 = float(input('Digite o Lado 02: '))
lado3 = float(input('Digite o Lado 03: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print('Essas Retas Formam um Triangulo EQUILATERO')
    elif lado1 != lado2 != lado3:
        print('Essas Retas formam um Triangulo ESCALENO')
    else:
        print('Essas Retas formam um Triangulo ISOSCELES')
else:
    print('Essas Retas nao formam um triangulo!')