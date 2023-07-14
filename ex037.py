'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e
3 para hexadecimal.'''

num = int(input("Digite um número qualquer: "))
choice = int(input('''Selecione a base de conversão:
[1] Binário
[2] Octal
[3] Hexadecimal '''))
if(choice == 1):
    print("{} em BINÁRIO: {}".format(num, bin(num)[2:]))
elif(choice == 2):
    print("{} em OCTAL: {}".format(num, oct(num)[2:]))
elif(choice == 3):
    print("{} em HEXADECIAL: {}".format(num, hex(num)[2:]))
else:
    print("Digite uma seleção válida!")