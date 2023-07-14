#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

frase = 'Year Calculator Tabajara'
print(frase)
print('-' * len(frase))
year = int(input("Enter any year: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("That's a leap year.")
else:
    print("That's not a leap year.")