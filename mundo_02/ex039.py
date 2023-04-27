from datetime import date

hoje = date.today()

print('=-' * 20)
print('Tempo pro alistamento')
print('=-' * 20)

anoUsuario = int(input('Digite seu ano de nascimento: '))
idadeUsuario = hoje.year - anoUsuario

if idadeUsuario > 18:
    print('Ja passou o tempo de se alistar!')
    print('Voce se alistou a {} anos'.format(idadeUsuario - 18))
elif idadeUsuario < 18:
    print('Voce ainda nao se alistou!')
    print('Falta {} anos pro seu alistamento'.format(18 - idadeUsuario))
else:
    print('Esse ano voce deve se alistar!')