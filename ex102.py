'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico
(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''


def fatorial(n, show=False):
    """
    Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: Opção de mostrar ou não a conta.
    :return: O valor do fatorialdo número desejado.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


num = int(input('Deseja o fatorial de qual número? '))
while True:
    try:
        resp = int(input('''Deseja ver todo o processo do cálculo? 
        Digite [1] para SIM
        Digite [2] para NÃO '''))
        if resp == 1 or resp == 2:
            break
    except ValueError:
        print('Digite um valor válido.')
if resp == 1:
    show = True
if resp == 2:
    show = False
print(fatorial(num, show))
help(fatorial)
