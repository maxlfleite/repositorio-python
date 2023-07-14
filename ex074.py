'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a
listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint
numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'The numbers were {numbers}.')
print(f'In order, they are {sorted(numbers)}.')
print('The numbers were: ', end='')
for n in numbers:
    print(f'{n} ', end='')
higher = lower = numbers[0]
for n in numbers:
    if n > higher:
        higher = n
    if n < lower:
        lower = n
print(f'\nThe highest number found was {higher}.')
print(f'The lowest number found was {lower}.')
print(f'The highest number found was {max(numbers)}.')
print(f'The lowest number found was {min(numbers)}.')