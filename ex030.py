#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print("Let's check if a number is odd or even:")
num = int(input("Enter any number: "))
if (num % 2 == 0):
    print("The number {} is even.".format(num))
else:
    print("The number {} is odd.".format(num))