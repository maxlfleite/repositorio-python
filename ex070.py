'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
gasto = mil = barato = 0
cheap = ' '
frase = '| Cadastro de Produtos |'
while True:
    print('-'*len(frase))
    print(frase)
    print('-' * len(frase))
    produto = str(input('Produto: ')).title()
    preco = float(input('Preço: R$ '))
    gasto = gasto + preco
    if preco >= 1000:
        mil = mil + 1
    if barato == 0:
        barato = preco
    if preco < barato:
        barato = preco
        cheap = produto
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Deseja cadastrar outro produto [S/N]? '))
    if resp in 'Nn':
        break
print('========== FIM DO PROGRAMA ==========')
print(f'O total gasto na compra: R$ {gasto:.2f}.')
print(f'Produtos acima de R$ 1000.00: {mil}.')
print(f'Produto mais barato: {cheap}.')
