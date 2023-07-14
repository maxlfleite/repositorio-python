#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o ângulo desejado: '))
seno = math.sin(math.radians(angulo))
print('Seno: {:.2f}'.format(seno))
cosseno = math.cos(math.radians(angulo))
print('Cosseno: {:.2f}'.format(cosseno))
tangente = math.tan(math.radians(angulo))
print('Tangente: {:.2f}'.format(tangente))

