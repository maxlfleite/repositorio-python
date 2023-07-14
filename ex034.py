'''Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

frase = 'Salary Calculator Tabajara'
print(frase)
print('-' * len(frase))
sal = float(input("How much does our slave make? $ "))
if(sal > 1250):
    newsal = sal + (sal * 0.1)
else:
    newsal = sal + (sal * 0.15)
print("Now our slave should make $ {:.2f}.".format(newsal))