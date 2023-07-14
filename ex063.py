#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

frase = "| Fibonnacci Demonstrator Tabajara |"
print('-'*len(frase))
print(frase)
print('-'*len(frase))
print(" ")
a = 0
b = 1
i = 3
num = int(input("How many number do you wish to see using Fibonnacci sequence? "))
print(f"{a} >>> {b} >>>", end = " ")
while i <= num:
    i = i + 1  
    c = b + a
    print(c, ">>>", end = ' ')
    a = b
    b = c
print("We have done it!")