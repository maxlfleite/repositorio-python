#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Informe o preço: R$ '))
desc = preco - (preco * 0.05)
print('Com 5% de desconto, você irá pagar apenas R$ {:.2f}.'.format(desc))
