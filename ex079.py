'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = list()
while True:
    while True:
        try:
            n = int(input("Enter a number: "))
            break
        except ValueError:
            print('Invalid input.', end=' ')
    if n in lista:
        print(f'Number {n} is already in the list. Enter another.')
    else:
        print('Number successfully added.')
        lista.append(n)
    while True:
        resp = str(input("Would you like to continue [Y/N]? "))
        if resp in "YyNn":
            break
    if resp in "Nn":
        break
print(f"Your list is: {sorted(lista)}.")


