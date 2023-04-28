num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite mais um valor: '))
num4 = int(input('Digite o ultimo valor: '))

tupla = (num1, num2, num3, num4)
pares = 0

print(f'Os valores digitados foram {tupla}')

if tupla.count(9) == 0:
    print('Nao tem nenhum 9 digitado')
else:
    print(f'O numero nove apareceu {tupla.count(9)} vezes')

if tupla.count(3) == 0:
    print('Nao tem nenhum numero tres')
else:
    print(f'O numero tres apareceu pela primeira vez na {tupla.index(3) + 1} posicao')

for c in range(0, len(tupla)):
    if tupla[c] % 2 == 0:
        print(f'Os numeros pares foram {tupla[c]}', end=' ')
        pares += 1

if pares == 0:
    print('Nao tem nenhum par!')

