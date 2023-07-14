'''Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triângulo.'''

frase = "Triangle Calculator Tabajara"
print(frase)
print("-" * len(frase))
print("Let's find out if we can make a triangle.")
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))
if ((a+b>c) and (b+c>a) and (c+a>b)):
    print("Alright! We can make a triangle with them.")
else:
    print("Sorry, mate. Triangle not possible.")