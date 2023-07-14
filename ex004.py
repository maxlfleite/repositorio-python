'''
programa que leia algo pelo telclado e mostre na tela 
o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

n = input("Digite alguma coisa: ")
print('Tipo primitivo desse valor: ', type(n))
print('So tem espaços? ', n.isspace())
print('É um número? ', n.isnumeric())
print("É alfabético? ", n.isalpha())
print("É alfanumérico? ", n.isalnum())
print('Está em maiúscula? ', n.isupper())
print('Está em minúsculas? ', n.islower())
print('Está capitalizada? ', n.istitle())
