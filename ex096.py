'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
'''
def area(a, b):
    r = a * b
    print(f'O terreno tem uma area de {r} m2.')


frase = ' Calculador de Terreno'
print(frase)
print('~'*len(frase))
largura = float(input('Digite a largura em m: '))
comprimento = float(input('Digite o comprimento em m: '))
area(largura, comprimento)
