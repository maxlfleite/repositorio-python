'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

frase = "Tabuation Calculator Tabajara"
print(frase)
print('='*len(frase))
num = int(input("Enter a number to show the multiplication table on the screen: "))
for c in range (1, 11):
    tab = num * c
    print(f"{num} x {c:2} = {tab}")
print("Thanks for using our Tabulation Calculator Tabajara.")
