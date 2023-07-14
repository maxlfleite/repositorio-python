'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista
ordenada na tela.'''
lista = []
for c in range (0,5):
    n = int(input('Enter a number: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Added by the end of the list...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Added at position {pos+1} of the list.')
                break
            pos += 1
print('~='*40)
print(f'Your list in order is: {lista}')
