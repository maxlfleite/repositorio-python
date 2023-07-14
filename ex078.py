'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
e o menor valor digitado e as suas respectivas posições na lista.'''
numbers = list()
for c in range(0, 5):
    numbers.append(int(input(f'Add the #{c+1} number to the list: ')))
print('You have entered these numbers: ')
highest = lowest = numbers[0]
h = l = 0
for i, c in enumerate(numbers):
    print(f'{c}... ', end='')
    if c > highest:
        highest = c
        h = i
    elif c < lowest:
        lowest = c
        l = i
print(f"\nThe list in order lowest to highest: {sorted(numbers)}.")
print(f'The list on order highest to lowest: {sorted(numbers, reverse=True)}.')
print(f'\nThe highest number in the list is {highest} at position {h+1}.')
print(f'The lowest number in the list is {lowest} at position {l+1}.')
