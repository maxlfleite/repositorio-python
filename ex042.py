'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que
tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

frase = 'Triangle Calculator Tabajara'
print(frase)
print('=' * len(frase))
sid1 = float(input("Digite o primeiro lado: "))
sid2 = float(input("Digite o segundo lado: "))
sid3 = float(input("Digite o terceiro lado: "))
if (sid1 + sid2 > sid3) and (sid1 + sid3 > sid2) and (sid2 + sid3 > sid1):
    print("Um triangulo é possível.")
    if (sid1 == sid2) and (sid2 == sid3):
        print("E ele será EQUILÁTERO.")
    elif (sid1 != sid2 and sid2 != sid3):
        print("E ele será ESCALENO.")
    elif (sid1 == sid2 and sid2 != sid3):
        print("E ele será ISÓCELES.")
    elif (sid1 != sid2 and sid2 == sid3):
        print("E ele será ISÓCELES.")
else:
    print("Um triangulo não é possível")




