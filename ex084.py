'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
heaviest = lightest = 0
people = []
data = list()
while True:
    data.append(str(input("Name: ")))
    data.append(float(input("Weigh in Kg: ")))
    if (len(people)) == 0:
        heaviest = lightest = data[1]
    else:
        if data[1] > heaviest:
            heaviest = data[1]
        if data[1] < lightest:
            lightest = data[1]
    people.append(data[:])
    data.clear()
    while True:
        resp = str(input("Would you like to continue[Y/N]? ")).strip().upper()[0]
        if resp in 'YN':
            break
    if resp == 'N':
        break
print('~='*40)
print(f'There are {len(people)} people in the list.')
for p in people:
    print(f'{p[0]} is {p[1]} Kg heavy.')
print('~='*40)
print(f'Highest weight: {heaviest:.1f} Kg. Heaviest people: ', end='')
for p in people:
    if p[1] == heaviest:
        print(f'/ {p[0]} / ', end='')
print(' ')
print(f'Lowest weight: {lightest:.1f} Kg. Lightest people: ', end='')
for p in people:
    if p[1] == lightest:
        print(f'/ {p[0]} / ', end='')
print('\n        ---------- The End ----------')
