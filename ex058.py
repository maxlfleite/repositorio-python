'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.'''
from random import randint
frase = '| Tabajara Games & Entretaiment |'
print("-"*len(frase))
print(frase)
print("-"*len(frase))
count = int(0)
num = randint(1, 100)
guess = int(input("Try to guess the number from 1 to 100 that I'm thinking of: "))
while guess != num:
    count = count + 1
    if guess > num:
        guess = int(input("Too high! Try again: "))
    elif guess < num:
        guess = int(input("Too low! Try again: "))
print(f"Congratulations! You've got the right number after {count} tries.")
