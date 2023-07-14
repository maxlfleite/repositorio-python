'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
saque = int(input("Valor do saque: R$ "))
nota50 = nota20 = nota10 = nota1 = 0
nota50 = saque // 50
saque = saque - (50 * nota50)
nota20 = saque // 20
saque = saque - (20 * nota20)
nota10 = saque // 10
saque = saque - (10 * nota10)
nota1 = saque // 1
print(f'''Total de notas:
R$ 50.00: {nota50}
R$ 20,00: {nota20}
R$ 10,00: {nota10}
R$ 1,00: {nota1}''')
