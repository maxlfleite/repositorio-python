'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores.
'''
from time import sleep
c = ('\033[m',          # 0 - blank (no color)
     '\033[0;30;41m',   # 1 - red
     '\033[0;30;42m',   # 2 - green
     '\033[0;30;43m',   # 3 - yellow
     '\033[0;30;44m',   # 4 - blue
     '\033[0;30;45m',   # 5 - purple
     '\033[7;30m')      # 6 - white


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[3], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca >>> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
