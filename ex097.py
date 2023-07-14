'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.
'''
def headline(msg):
    c = '~' * len(msg) + 4
    print(c)
    print(f'  {msg}')
    print(c)


titulo = str(input('Título: '))
headline(titulo)
