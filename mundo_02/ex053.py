palavra = str(input('Digite uma palavra: '))
palavraSemEspaco = palavra.replace(' ', '')
palavraInvertida = palavraSemEspaco[::-1]

if palavraInvertida == palavraSemEspaco:
    print('E uma palindromo')
else:
    print('Nao e um palindromo')