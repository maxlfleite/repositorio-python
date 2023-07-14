'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = list()
while True:
    while True:
        try:
            lista.append(int(input('Add a number to you list: ')))
            break
        except ValueError:
            print("Invalid input! ", end="")
    while True:
        resp = str(input("Would you like to continue [Y/N]? ")).strip().upper()[0]
        if resp in 'YN':
            break
    if resp == 'N':
        break
print(f"You have entered {len(lista)} numbers.")
print(f"Your list in reverse order is {sorted(lista, reverse = True)}.")
v = 0
for n in lista:
    if n == 5:
        v += 1
print(f"The number 5 was found {v} times.")
