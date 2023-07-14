'''Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos.'''
maior = int(0)
menor = int(9999)
frase = "Weigh Analizator Tabajara"
print("-"*len(frase))
print(frase)
print("-"*len(frase))
for c in range (1, 6):
    peso = float(input(f"Digite o peso da {c}ª pessoa: "))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f"O maior peso encontrado foi {maior:.1f} e o menor foi {menor:.1f}")