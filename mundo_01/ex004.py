item = input('Digite qualquer coisa: ')

print('O tipo primitivo é {}'.format(type(item)))
print('é alfa-numerico? {}'.format(item.isalpha()))
print('é um numero? {}'.format(item.isnumeric()))
print('É uma letra? {}'.format(item.isalpha()))
print('Só tem maisculas? {}'.format(item.isupper()))
print('Só tem minusculas? {}'.format(item.islower()))
print('Só tem espaços? {}'.format(item.isspace()))
print('Está capitalizada? {}'.format(item.istitle()))
