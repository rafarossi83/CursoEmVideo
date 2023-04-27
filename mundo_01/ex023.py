numero = int(input('Digite um numero de 0 a 9999: '))
# Extrai o milhar, centena, dezena e unidade
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = ((numero % 1000) % 100) // 10
unidade = ((numero % 1000) % 100) % 10

# Imprime o resultado
print("Milhar:", milhar)
print("Centena:", centena)
print("Dezena:", dezena)
print("Unidade:", unidade)
