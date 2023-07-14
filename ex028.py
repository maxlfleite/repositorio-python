#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
num = randint(1,100)
guess = int(input('Try to find out which number I am thinking: '))
while (guess != num):
    if (guess > num):
        print('Too high!')
        guess = int(input("I'll give you another chance: "))
    if (guess < num):
        print('Too low!')
        guess = int(input("I'll give you another chance: "))
if not():
    print("Congratulations! You've got the right number.")

