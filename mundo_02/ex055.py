maior = 0
menor = 0

for i in range(1, 6):
    
    peso = float(input('Digite o Peso: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso

print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))