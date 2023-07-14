#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Qual o nome do aluno? ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('')
print('A média de {} é {:.2f}.'.format(nome, media))
