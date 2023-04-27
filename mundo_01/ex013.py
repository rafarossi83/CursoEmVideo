salarioOriginal = float(input('Digite o valor do sálario: '))

aumento = salarioOriginal * 15 / 100
novoSalario = salarioOriginal + aumento

print('O sálario de R${:.2f} agora custará R${:.2f}'.format(salarioOriginal, novoSalario))