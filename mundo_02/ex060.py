resultado = 1
num = int(input('Digite um numero: '))
numOriginal = num

while num != 0:
    resultado *= num
    num -= 1
print('O fatorial de {} e {}'.format(numOriginal, resultado))
