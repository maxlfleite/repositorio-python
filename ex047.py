'''Crie um programa que mostre na tela todos os números pares que estão no intervalo
entre 1 e 50.'''

frase = 'Even Calculator Tabajara'
print(frase)
print('-'*len(frase))

for c in range (1, 51):
    if c % 2 == 0:
        print(c)
print ("ACABOOOOOU!!! ACABOOOOOU!!! É TETRAAAAAA!!!")

''' Solução para exigir menos da máquina:
for c in range (2, 51, 2):
    print(c)
print("Finished!!!")'''
