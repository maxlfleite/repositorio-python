'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
lista = list()
dicio = dict()
add = average = 0
while True:
    dicio["Name"] = str(input("Name: "))
    dicio["Age"] = int(input("Age: "))
    add = add + dicio["Age"]
    while True:
        try:
            dicio["Gender"] = str(input("Gender [M/F]: ")).strip().upper()[0]
            if dicio["Gender"] in "MF":
                break
        except ValueError:
            print("Invalid input", end='')
    lista.append(dicio.copy())
    dicio.clear()
    while True:
        resp = str(input("Would you like to register another person [Y/N]? ")).strip().upper()[0]
        if resp in "YN":
            break
    if resp == 'N':
        break
print('~='*30)
print(f'A. There were {len(lista)} people registered.')
average = add / len(lista)
print(f'B. The average age is {average:.1f}.')
print('C. All women registered:', end='')
for w in lista:
    if w["Gender"] == 'F':
        print(f' - {w["Name"]}', end='')
print()
print('D. People who are over the average age: ')
for a in lista:
    if a["Age"] >= average:
        print('  ', end='')
        for k, v in a.items():
            print(f'{k} = {v}; ', end='')
        print()
print(' <<< Program Shutting Down >>>')
