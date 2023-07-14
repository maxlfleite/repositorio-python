#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
frase = 'Jokepo Game Tabajara' 
jogador = int(input('''Escolha sua opção:
[1] Pedra
[2] Papel
[3] Tesoura '''))
print('JO')
sleep(1)
print('KE')
sleep(1)
print('PO!!!')
sleep(1)
if computador == 0:
    if jogador == 1:
        print("EMPATE!!!")
    elif jogador == 2:
        print("Tu é fraco. Eu, computador, ganhei! =P")
    elif jogador == 3:
        print("Não acredito que você me venceu. Parabéns!!!")
elif computador == 1:
    if jogador == 1:
        print("Tu é fraco. Eu, computador, ganhei! =P")
    elif jogador == 2:
        print("EMPATE!!!")
    elif jogador == 3:
        print("Não acredito que você me venceu. Parabéns!!!")
elif computador == 2: 
    if jogador == 1:
        print("Não acredito que você me venceu. Parabéns!!!")
    elif jogador == 2:
        print("Tu é fraco. Eu, computador, ganhei! =P")
    elif jogador == 3:
        print("EMPATE!!!")

print("Eu escolhi {}.".format(itens[computador]))