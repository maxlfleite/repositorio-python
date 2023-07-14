'''
 Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
 que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
 crescente.
'''
listas = [[], []]
number = 0
for i in range(1, 8):
    number = (int(input("Enter a number: ")))
    if number % 2 == 0:
        listas[0].append(number)
    else:
        listas[1].append(number)
print(f'The list of even numbers: {sorted(listas[0])}')
print(f'The list of odd numbers: {sorted(listas[1])}')
