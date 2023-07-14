'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''
frase = "| Spetacular Calculator Tabajara |"
print("~"*len(frase))
print(frase)
print("~"*len(frase))
print(" ")
num = 0
add = 0
a = 0
print("The number 999 stops the program!")
while num != 999:
    num = int(input("Enter a number to sum: "))
    if num != 999:
        a = a + 1
        add = add + num
    else:
        print("You chose to stop the program.")
print(f"The sum of all the {a} numbers entered is {add}.")