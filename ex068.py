'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
frase = '| Tabajara Games and Entertainment |'
print('='*len(frase))
print(frase)
print('='*len(frase))
count = 0
while True:
    choice = str(input('Would you like odds or evens [O/E]? ')).strip().upper()
    while choice not in 'OoEe':
        choice = str(input('Please, enter a valid option: Odds or Evens [O/E] '))
    user = int(input('Choose a number: '))
    pc = randint(1, 9)
    num = user + pc
    if num % 2 == 0:
        game = 'EVEN'
    else:
        game = 'ODD'
    if choice in game:
        count += 1
        print('~'*60)
        print('You WIN!!!')
        print(f'You played {user} and the computer {pc}. Total {num}. Result: {game}')
        print('~' * 60)
        print("Let's play again")
        print('=~'*30)
    else:
        print('~' * 60)
        print('You LOOSE!!!')
        print(f'You played {user} and the computer {pc}. Total {num}. Result: {game}')
        print('~' * 60)
        break
print(f'Game over! You won {count} times.')
