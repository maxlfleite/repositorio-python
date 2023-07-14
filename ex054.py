'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.'''
import datetime
f = 'People Analizator Tabajara'
print('-'*len(f))
print(f)
print('-'*len(f))
maior = int(0)
menor = int(0)
for c in range (1, 8):
    nasc = int(input(f"Digite o ano de nascimento da {c}ª pessoa: "))
    age = datetime.date.today().year - nasc
    print (f"Esta criatura tem {age} anos de idade.")
    if age >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print (f"Total de maiores de idade: {maior}")
print (f"Total de menores de idade: {menor}")