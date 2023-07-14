#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = str(input('Digite seu nome completo: ')).strip().title()
print('Prazer em te conhecer.')
namesplit = name.split()
print('Seu primeiro nome é {}.'.format(namesplit[0]))
print('Seu último nome é {}.'.format(namesplit[len(namesplit)-1]))
