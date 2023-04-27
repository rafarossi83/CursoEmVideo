salarioAtual = float(input('Qual o salário atual: '))

if salarioAtual >= 1250:
    reajuste = (10 * salarioAtual)  / 100
    salarioNovo = salarioAtual + reajuste
else: 
    reajuste = (15 * salarioAtual) / 100
    salarioNovo = salarioAtual + reajuste
    
print('Salário do Funcionarios')
print('Valor Antigo: R${:.2f}\nValor Novo: R${:.2F}'.format(salarioAtual, salarioNovo))