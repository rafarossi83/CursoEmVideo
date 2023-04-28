# para este exercicio estou usando a tabela de 2022 ja que a chapecoence (como o enunciado pede) nao ficou entre os 20 primeiros em 2023

times = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio', 'Athletico Paranaense', 'Santos', 'São Paulo', 'Internacional', 'Fluminense', 'Corinthians',
         'Fortaleza', 'Bahia', 'Ceará', 'Cruzeiro', 'América Mineiro', 'Atlético Goianiense', 'Chapecoense', 'Botafogo', 'Vasco da Gama', 'Red Bull Bragantino')

print('=' * 25)
print(f'Os cinco primeiros colocados: {times[0:5]}')
print(f'Os quatro ultimos colocados: {times[:-5:-1]}')
print('=' * 25)
print('Times em Ordem Alfabetica:')
print(sorted(times))
print('=' * 25)
print(f'Posicao Chapecoence: {times.index("Chapecoense") + 1}')
