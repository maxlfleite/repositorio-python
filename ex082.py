'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista = list()
listapar = []
listaimpar = []
while True:
    while True:
        try:
            lista.append(int(input("Enter a number to add to your list: ")))
            break
        except ValueError:
            print("Invalid input! ")
            print('~='*30)
    while True:
        resp = str(input("Would you like to continue [Y/N]? ")).strip().upper()[0]
        if resp in 'YN':
            break
    if resp == 'N':
        break
print('_-'*30)
print(f"This is your list: {lista}.")
for n in lista:
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
print(f"This is your even list: {listapar}.")
print(f"This is your odd list: {listaimpar}.")
print('_-'*30)
