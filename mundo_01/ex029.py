velocidade = float(input('Digite a velocidade: '))

if velocidade >= 80:
    print('Veiculo Multado!')
    print('Valor da Multa: R${:.2f}'.format((velocidade - 80) * 7))
else:
    print('Veiculo dentro do Limite!')