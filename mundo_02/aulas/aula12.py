nome = str(input('Qual o seu nome: '))

if nome == 'Rafael':
    print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome e bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que belo nome feminino!')
else:
    print('Que nome comum!')
    
print('Tenha um bom dia, {}!'.format(nome))