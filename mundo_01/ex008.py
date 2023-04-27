m = float(input('Digite um valor em metros: '))

dm = m * 10
cm = m * 100
mm = m * 1000
km = m / 1000
hm = m / 100
dam = m / 10


print('=-' * 20)
print('Conversão de Metros')
print('=-' * 20)

print('{} metros equivale a: '.format(m))
print('Decímetro: {}\nCentímetro: {}\nMilímetro: {}'.format(dm, cm, mm))
print('Quilômetro: {}\nHectômetro: {}\nDecametro: {}'.format(km, hm, dam))