'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''

frase = 'Price Calculator Tabajara'
print(frase)
print('-'*len(frase))
preco = float(input("Qual o preço do item? R$ "))
choice = int(input('''Escolha a forma de pagamento:
[1] À vista no dinheiro ou pix: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em 2x no cartão sem juros
[4] 3x ou mais no cartão: 20% de juros '''))

if choice == 1:
    pag = preco - (preco * 0.1)
    print('''Você escolheu o melhor plano.
Você irá pagar R$ {:.2f}'''. format(pag))
elif choice == 2:
    pag = preco - (preco * 0.05)
    print("Você irá pagar R$ {:.2f}".format(pag))
elif choice == 3:
    parcela = preco / 2
    print("Você irá pagar o valor normal dividido em 2x de R$ {:.2f}.".format(parcela))
elif choice == 4:
    pag = preco + (preco * 0.2)
    prazo = int(input("Deseja dividir em quantas vezes? "))
    parcela = pag / prazo
    print("Você pagará uma parcela de R$ {:.2f} em {}x totalizando R$ {:.2f}.".format(parcela, prazo, pag))
