'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valorcorreto.'''

sex = str(input("Enter a gender [M/F]: ")).strip().upper()[0]
while sex not in 'MmFf':
    sex = str(input("Invalid gender. Please, choose a correct one [M/F]: ")).strip().upper()[0]
print(f"You have chosen {sex}.")
print("Muchas Gracias and always come back.")