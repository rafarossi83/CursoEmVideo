dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km percorridos? '))

valorTotal = (60 * dias) + (0.15 * km)

print('O total a pagar é: R${:.2f}.'.format(valorTotal))