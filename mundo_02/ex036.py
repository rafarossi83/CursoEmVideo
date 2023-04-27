salario = float(input('Digite o valor do seu salario: '))
valorCasa = float(input('Digite o valor da casa: '))
tempoAno = int(input('Em quantos anos pretende pagar: '))

tempoMes = tempoAno * 12
valorParcela = valorCasa / tempoMes
condicao = (30 * salario) / 100

if condicao <= valorParcela:
    print('Emprestimo \033[31m'+'NEGADO'+'\033[0;0m')
    print('O valor da parcela supera 30% do seu salario')
else:
    print('Emprestimo \033[32m'+'APROVADO'+'\033[0;0m')
print('Parcela Mensal: {:.2f}'.format(valorParcela))

