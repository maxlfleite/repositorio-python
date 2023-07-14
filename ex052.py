'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

f = 'Cousin Number Calculator Tabajara'
print(f)
print('='*len(f))
count = int(0)
num = int(input("Digite um número: "))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end = ' ')
        count = count + 1
    else:
        print('\33[31m', end = ' ')
    print(f'{c}', end = ' ')
print(f'\n\033[mO número {num} foi divisível {count} vezes.')
if count == 2:
    print("Por isso ele é PRIMO!!!")
else:
    print("Por isso ele não é PRIMO!!!")
