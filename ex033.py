'''Faça um programa que leia três números e mostre qual é o maior
e qual é o menor.'''
highest = int(0)
lowest = int(9999)
num1 = int(input("Enter the first number: "))
if highest < num1:
    highest = num1
if lowest > num1:
    lowest = num1
num2 = int(input("Enter the second number: "))
if highest < num2:
    highest = num2
if lowest > num2:
    lowest = num2

num3 = int(input("Enter the third number: "))
if highest < num3:
    highest = num3
if lowest > num3:
    lowest = num3
print("The highest number typed was {} and the lowest was {}.".format(highest, lowest))
