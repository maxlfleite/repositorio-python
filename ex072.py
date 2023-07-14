'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até
vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''


numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
           'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    try:
        user = int(input("Enter a number between 0 and 20: "))
        if 0 <= user <= 20:
            break
    except ValueError:
        print("Invalid input. Please, enter a valid one.")
print(f"You have entered the number {numbers[user]}")

