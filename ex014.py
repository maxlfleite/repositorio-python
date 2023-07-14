#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Temperatura em ºC: '))
fahr = (celsius * 1.8) + 32
print('Temperatura em Fahrenheit: {} ºF.'.format(fahr))
kelvin = celsius + 273.15
print('Temperatura em Kelvin: {} k.'.format(kelvin))
