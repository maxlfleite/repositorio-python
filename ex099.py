'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep
def maior(*num):
    cont = maior = 0
    print('~='*30)
    print('Analizando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 2, 1)

