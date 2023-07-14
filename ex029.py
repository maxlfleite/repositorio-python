'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''
print("==Ultra Multador Tabajara==")
speed = int(input("At what speed was the car in Km/h? "))
if(speed <= 80):
    print("Well done! Keep driving safely!")
else:
    ticket = (speed - 80) * 7
    print("Busted!!! You'll pay a $ {:.2f} ticket!".format(float(ticket)))
