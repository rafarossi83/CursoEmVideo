from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0,10), randint(0, 10), randint(0, 10))

print(f'Os numeros sorteados foram: {tupla}')
print(f'O menor valor e {sorted(tupla)[0]}')
print(f'O maior valor e {sorted(tupla)[-1]}')