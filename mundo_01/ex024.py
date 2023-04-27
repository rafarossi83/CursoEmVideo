cidade = input('Digite o nome da cidade: ').upper().strip()


if cidade[0:5] == 'SANTO':
    print('A cidade {} começa com Santo'.format(cidade))
    print(cidade[0:5])
else:
    print('A cidade {} não começa com Santo!'.format(cidade))
    print(cidade[0:5])