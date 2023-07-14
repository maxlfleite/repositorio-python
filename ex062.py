'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''
frase = "| PA Demonstrator Tabajara |"
print("-"*len(frase))
print(frase)
print("-"*len(frase))
num = int(input("Primeiro termo da sua PA: "))
raz = int(input ("Razão da sua PA: "))
user = 10
a = 0
while user != 0:
    cont = 1
    while cont <= user:
        a = a + 1
        print(f"{num} >>>", end = " ")
        num = num + raz
        cont = cont + 1
    print("PAUSA...")
    user = int(input("Deseja mostrar mais quantos números? "))
    count = 1
print(f"Foram mostrados {a} números.")
    
    
    
    
    
    
    