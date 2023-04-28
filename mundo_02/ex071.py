notas50 = notas20 = notas10 = notas1 = 0

print('=' * 25)
print('BANCO RAFAEL')
print('=' * 25)

valorSacado = int(input('Qual o valor de saque? R$'))

while True:
    notas50 = valorSacado // 50
    valorSacado %= 50
    notas20 = valorSacado // 20
    valorSacado %= 20
    notas10 = valorSacado // 10
    valorSacado %= 10
    notas1 = valorSacado // 1
    break

print(f'Total de {notas50} notas de R$50')
print(f'Total de {notas20} notas de R$20')
print(f'Total de {notas10} notas de R$10')
print(f'Total de {notas1} notas de R$1')
print('=' * 25)
print('Volte sempre ao Banco Rafael, tenha um bom dia!')