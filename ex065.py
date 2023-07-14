'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
frase = "| Spetacular Calculator Tabajara |"
print("~"*len(frase))
print(frase)
print("~"*len(frase))
print(" ")
resp = 'S'
add = higher = count = lower = 0
while resp not in "Nn":
    num = int(input("Enter a number: "))
    count = count + 1
    add = add + num
    if count == 1:
        higher = lower = num
    else:
        if num > higher:
            higher = num
        elif num < lower:
            lower = num
    resp = str(input("Would you like to continue [Y/N]? ")).strip().upper()[0]
media = add / count
print(f"There were {count} numbers entered and the average was {media:.1f}")
print(f"The highest number was {higher} and the lowest {lower}.")
