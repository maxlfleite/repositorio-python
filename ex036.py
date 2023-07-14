'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input("Qual o valor do imóvel? R$ "))
salario = float(input("Qual sua renda mensal? R$ "))
prazo = int(input("Em quantos meses deseja pagar? "))
valorprazo = casa / prazo
aprovado = salario * 0.3
print("Valor da prestação: R$ {:.2f}".format(prazo))
if (aprovado >= valorprazo):
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado.")
