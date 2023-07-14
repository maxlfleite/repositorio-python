#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Dolar no dia do exercicio (24/05/2023)
dol = float(input('Quantos dolares você gostaria de comprar? US$ '))
reais = dol * 4.95
print('')
print('Para comprar US$ {:.2f} você precisará de R$ {:.2f}.'.format(dol, reais))

