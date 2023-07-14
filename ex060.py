#Faça um programa que leia um número qualquer e mostre o seu fatorial.
frase = "| Fatorial Calculator Tabajara |"
print("-"*len(frase))
print(frase)
print("-"*len(frase))
print(' ')
a = int(input("Enter a number to calculate its factorial: "))
b = a
fac = 1
while a > 0:
    fac = fac * a
    print(f"{a}", end = " ")
    print(" x " if a > 1 else " = ", end = " ")
    a = a - 1
print(f"{fac}")
print(f"{b}! = {fac}")