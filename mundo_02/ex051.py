termo = int(input('Digite o Termo: '))
razao = int(input('E qual a Razao: '))
decimo = termo + (10 - 1) * razao

for i in range(termo, decimo, razao):
    print(i, end='→')
print('ACABOU')