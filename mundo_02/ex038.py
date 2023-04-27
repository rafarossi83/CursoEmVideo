print('=-' * 20)
print('Descubra o numero maior!')
print('=-' * 20)

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

if num1 > num2:
    print('O numero {} e maior que {}'.format(num1, num2))
elif num2 > num1:
    print('O numero {} e maior que {}'.format(num2, num1))
else:
    print('Os dois numeros sao iguais')