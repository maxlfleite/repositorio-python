'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500.'''

frase = 'Calculator Tabajara'
print(frase)
print('-'*len(frase))
add = int(0)
count = int(0)
for c in range (1,501):
    if c % 3 == 0:
        count = count + 1
        add = add + c
print("The total amount from adding all {} numbers multiples of 3 is {}.".format(count, add))
