'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um 
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

''' Solução sem importação
co = float(input('Comprimento cateto oposto: '))
ca = float(input('Comprimento cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('Comprimento da hipotenusa: {:.2f}'.format(hi))

Solução com importação do math completo
import math
co = float(input('Comprimento cateto oposto: '))
ca = float(input('Comprimento cateto adjacente: '))
hi = math.hypot(co,ca)
print('Comprimento da hipotenusa: {:.2f}'.format(hi))

'''
from math import hypot
co = float(input('Comprimento cateto oposto: '))
ca = float(input('Comprimento cateto adjacente: '))
hi = hypot(co,ca)
print('Comprimento da hipotenusa: {:.2f}'.format(hi))
