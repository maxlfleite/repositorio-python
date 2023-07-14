'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
200Km e R$0,45 parta viagens mais longas.'''

print("Traveler Calculator Tabajara")
print('-' * 28)
distance = float(input("How far will you travel in Km? "))
if (distance <= 200.0):
    price = distance * 0.5
    print("You'll pay $ {:.2f}.".format(price))
else:
    price = distance * 0.45
    print("You'll pay $ {:.2f}.".format(price))