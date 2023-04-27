palavra = input('Digite uma palavra: ').upper().strip()

print('A letra "A" aparece {} vezes'.format(palavra.count('A')))
print('Ela aparece pela primeira na {}° posição'.format(palavra.find('A') + 1))
print('E pela ultima vez na {}° posição'.format(palavra.rfind('A') + 1))