distancia = float(input('Digite a distância da viagem: '))

if distancia <= 200:
    print('Valor por Km: R$0.50\nValor Total da Viagem: R${:.2f}'.format(distancia * 0.50))
else: 
    print('Valor por Km: R$0.45\nValor Total da Viagem: R${:.2f}'.format(distancia * 0.45))