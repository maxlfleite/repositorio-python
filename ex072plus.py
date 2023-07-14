numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
           'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    while True:
        try:
            user = int(input("Enter a number between 0 and 20: "))
            if 0 <= user <= 20:
                break
        except ValueError:
            print("Invalid input. Please, enter a valid one.")
    print(f"You have entered the number {numbers[user]}")
    while True:
        resp = str(input("Would you like to run the program again [Y/N]? ")).strip().upper()[0]
        if resp in 'YyNn':
            break
    if resp in 'Nn':
        break
print('Thanks for using our program.')
