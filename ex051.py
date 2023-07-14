'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

f = 'Progressão Aritimetica Calculator Tabajara'
print(f)
print('='*len(f))
num = int(input("Digite o primeiro termo da PA: "))
raz = int(input("Agora digite a razão da PA: "))
decimo = num + (10 - 1) * raz
for c in range (num, decimo + raz, raz):
    print(c, end = ' -> ' )
print("Muchas gracias e volte sempre!")
