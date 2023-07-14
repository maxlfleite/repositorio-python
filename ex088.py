'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
composta.
'''
from random import randint
from time import sleep
lista = []
jogos = []
print('~='*20)
print('               JOGOS DA MEGA SENA  ')
print('~='*20)
quant = int(input('Quantos jogos você deseja que eu sortei? '))
for i in range(0, quant):
    for j in range(0, 6):
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('~='*3, f'SORTEANDO {quant} JOGOS ', '~='*3)
for a, b in enumerate(jogos):
    print(f'Jogo {a+1}: {b}')
    sleep(1)
print('~='*5, '<BOA SORTE>', '~='*5)
