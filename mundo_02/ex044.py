valorProduto = float(input('Digite o Valor do Produto: ').strip())
formaPagamento = int(input('1 - A vista (dinheiro/cheque)\n2 - A vista no Cartao\n3 - Em ate 2x no Cartao\n4 - 3x ou mais no Cartao\nSelecione uma modalidade: ').strip())

if formaPagamento == 1:
    desconto = (valorProduto * 10) / 100
    print('Valor Produto: R${:.2f}\nDesconto: R${}\nValor Final: R${:.2f}'.format(valorProduto, desconto, valorProduto - desconto))
elif formaPagamento == 2:
    desconto = (valorProduto * 5) / 100
    print('Valor Produto R${:.2f}\nDesconto: R${}\nValor Final R${:.2f}'.format(valorProduto, desconto, valorProduto - desconto))
elif formaPagamento == 3:
    print('Neste modalidade nao oferecemos desconto!\nValor Total: R${:.2f}'.format(valorProduto))
elif formaPagamento == 4:
    juros = (valorProduto * 20) / 100
    print('Valor Produto: R${:.2f}\nJuros: R${}\nValor Final: {:.2f}'.format(valorProduto, juros, valorProduto + juros))
else:
    print('Opcao Invalida, Tente Novamente')