'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

frase = 'IMC Calculator Tabajara'
print(frase)
print('='*len(frase))
peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura * altura)
print("Seu IMC: {:.1f}".format(imc))
if imc < 18.5:
    print("Vai comer, desgraça... Tais mago demai...")
elif imc >= 18.5 and imc < 25:
    print("Tem alguém indo pra academia direitinho. Tá de parabéns. Peso ideal.")
elif imc >= 25 and imc < 30:
    print("Ta bom de começar a fechar boquinha e ir malhar. Tá acima do peso.")
elif imc >= 30 and imc < 40:
    print("Bicho, na moral, tu ainda consegue ver teu pinto? Ta gordo demais, véi...")
elif imc >= 40:
    print("Desgraça, tu ainda consegue lavar a bunda? Bicho gordo da porra. Tu vai infartar, danado.")
