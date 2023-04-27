nome = str(input('Digite um Nome: ')).strip()
lista = nome.split()

print(nome.upper())
print(nome.lower())
print('O nome {} possui {} letras'.format(nome, len(nome.replace(' ', ''))))
print('O nome {} possui {} caracteres'.format(lista[0], len(lista[0])))
