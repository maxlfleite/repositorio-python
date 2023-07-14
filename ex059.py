'''Crie um programa que leia dois valores e mostre um menu na tela:'''
from time import sleep
frase = "| Fantastic Calculator Tabajara |"
print('-'*len(frase))
print(frase)
print('-'*len(frase))
print(' ')
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
resp = int(1)
while resp != 5:
    resp = int(input('''What to do next?
    [1] Sum
    [2] Multiply
    [3] Show higher
    [4] New Numbers
    [5] Leave Program
>>>Enter a valid code: '''))
    if resp > 5:
        print("Invalid code! Please, choose a valid one!")
        print('-'*len(frase))
    elif resp == 1:
        add = num1 + num2
        print(f"The sum of {num1} and {num2} is {add}.")
        print('-'*len(frase))
    elif resp == 2:
        mult = num1 * num2
        print(f"The multiplication of {num1} and {num2} is {mult}.")
        print('-'*len(frase))
    elif resp == 3:
        if num1 > num2:
            print(f"{num1} is higher than {num2}.")
            print('-'*len(frase))
        if num2 > num1:
            print(f"{num2} is higher than {num1}.")
            print('-'*len(frase))
    elif resp == 4:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print('-'*len(frase))
    sleep(2)
print('-'*len(frase))
print("Thanks for using Fantastic Calculator Tabajara.")

