'''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Nome maiúsculo: {}'.format(nome.upper()))
print('Nome minúsculo: {}'.format(nome.lower()))
print('Seu nome tem {} letras ao total.'.format(len(nome) - nome.count(' ')))
nomesplit = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format((nomesplit[0]), len(nomesplit[0])))
