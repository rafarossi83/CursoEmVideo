numero = ''
maior = ''
menor = ''
somador = 0
cont = 0
continuar = 'S'

print('=-' * 20)
print('Bem vindo ao calculo de medias!')
print('=-' * 20)

while continuar != 'N':
    numero = int(input('Digite um numero aleatorio: ').strip())
    if cont == 0:
        maior = numero
        menor = numero
    somador += numero
    cont += 1
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    continuar = str(input('Deseja continuar? [S / N]: ')).upper().strip()[0]

print('A media dos numeros digitados vale {}'.format(somador / cont))
print('Maior numero: {}\nMenor numero: {}'.format(maior, menor))