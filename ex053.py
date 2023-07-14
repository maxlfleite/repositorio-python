'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.'''
f = 'Palídromo Identificator Tabajara'
print(f)
print('='*len(f))
inverso = ''
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}.")
if inverso == junto:
    print("Temos um palídromo.")
else:
    print("Não é um palídromo.")