'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.'''
frase = "| PA Demonstrator Tabajara |"
print("-"*len(frase))
print(frase)
print("-"*len(frase))
num = int(input("Primeiro termo da sua PA: "))
raz = int(input ("Razão da sua PA: "))
cont = 1
while cont <= 10:
    print(f"{num} >>>", end = " ")
    num = num + raz
    cont = cont + 1
print("We have done it!!!")
    
'''dez = num + (10 - 1) * raz
while num <= dez:
    print(f"{num} >>>", end = ' ')
    num = num + raz
print("We have done it!!!")'''

    