soma = cont = num = 0

print('=-' * 20)
print('Somador de Numeros\nDigite 999 para parar!')
print('=-' * 20)

while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores vale {soma}!')


