numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'novo', 'dez',
           'onze', 'doze', 'treze', 'quartorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um numero entre 0 e 20: '))

while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um numero de 0 a 20: '))

print(f'Voce digitou o numero {numeros[num]}')