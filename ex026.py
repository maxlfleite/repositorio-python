#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite seu texto: ')).strip().upper()
print('Existem {} letras [a] no seu texto.'.format(frase.count('A')))
print('O primeiro [a] aparece na posição {}.'.format(frase.find('A')+1))
print('O último [a] aparece na posição {}.'.format(frase.rfind('A')+1))
