altura = float(input('Digite sua Altura: '))
peso = float(input('Digite seu Peso: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo de Peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso Ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')