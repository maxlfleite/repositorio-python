'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
frase = '| People Cadastrator Tabajara |'
roun = round(len(frase) / 2)
print('=~' * roun)
print(frase)
print('=~' * roun)
more18 = 0
male = 0
female20 = 0
while True:
    print('-'*60)
    age = int(input("Age: "))
    gender = str(input("Gender [M/F]: ")).strip().upper()
    while gender not in "mMfF":
        gender = str(input('Please, enter a valid gender [M/F] ')).strip().upper()
    if age >= 18:
        more18 += 1
    if gender in 'Mm':
        male += 1
    if gender in 'Ff':
        if age < 20:
            female20 += 1
    print(' ')
    resp = str(input('Would you like to register another person [Y/N]? ')).strip().upper()
    while resp not in "yYnN":
        resp = str(input("Please, choose a valid option [Y/N]: ")).strip().upper()
    if resp in 'Nn':
        break
print('~'*60)
print(f'There were {more18} people 18 or over registered.')
print(f'There were {male} males registered.')
print(f'There were {female20} females under the age of 20 registered.')