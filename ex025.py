#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

name = str(input('Digite seu nome completo: ')).strip().upper()
print('Existe Silva no seu nome? {}'.format('SILVA' in name))
