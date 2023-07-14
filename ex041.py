'''041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''
age = int(input("How old is the swimmer? "))
if age >= 9 and age < 14:
    print("Competidor da categoria MIRIM.")
elif age >= 14 and age < 19:
    print("Competidor da categoria INFANTIL.")
elif age >= 19 and age < 25:
    print("Competidor da categoria JÚNIOR.")
else:
    print("Competidor da categoria MASTER.")
