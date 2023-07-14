'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
f = 'Even calculator Tabajara'
print(f)
print('='*len(f))
add = int(0)
count = int(0)
for c in range (1, 7):
    num = int(input("Enter any number: "))
    if (num % 2 == 0):
        count = count + 1
        add = add + num
    else:
        add = add + 0
print(f'There were {count} even numbers and their sum is {add}.')
