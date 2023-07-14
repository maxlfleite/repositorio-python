'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
numbers = (int(input('Enter the first number: ')),
           int(input('Enter the second number: ')),
           int(input('Enter the third number: ')),
           int(input('Enter the fouth number: ')))
print(f'You have entered the numbers {numbers}.')
print(f'The number 9 was entered {numbers.count(9)} times.')
if 3 in numbers:
    print(f'The number 3 was entered in the #{numbers.index(3)+1} position.')
else:
    print('The number 3 was not entered.')
print('The even numbers entered were: ')
for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')