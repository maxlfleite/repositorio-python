#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salário atual do funcionário? R$ '))
ajuste = salario + (salario * 0.15)
print('O novo salário reajustado será de R$ {}.'.format(ajuste))
