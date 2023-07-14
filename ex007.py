# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite o valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('')
print('Teremos:')
print('{} kilometros.'.format(km))
print('{} hectômetro.'.format(hm))
print('{} decâmetro.'.format(dam))
print('{} decímetro.'.format(dm))
print('{} centímetros.'.format(cm))
print('{} milímetros.'. format(mm))
