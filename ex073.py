'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
drivers = ('Max Verstappen', 'Charles Leclerc', 'Sergio Perez', 'George Russell', 'Carlos Sainz', 'Lewis Hamilton',
            'Lando Norris', 'Esteban Ocon', 'Fernando Alonso', 'Valtteri Bottas', 'Daniel Ricciardo',
           'Sebastian Vettel', 'Kevin Magnussen', 'Pierre Gasly', 'Lance Stroll', 'Mick Schumacher', 'Yuki Tsunoda',
           'Zhou Guanyu', 'Alexander Albon', 'Nicholas Latifi', 'Nyck De Vries', 'Nico Hulkenberg')
frase = '| F1 2022 DRIVER STANDINGS |'
print('-' * len(frase))
print(frase)
print('-' * len(frase))
print(' ')
while True:
    while True:
        print('[1] Top 5')
        print('[2] Last 4')
        print('[3] Drivers in Alphabetical Order')
        print("[4] Fernando Alonso's Standing")
        while True:
            try:
                choice = int(input("Enter your option: "))
                if 0 < choice < 5:
                    break
            except ValueError:
                print('Please, enter a valid option.')
        if choice == 1:
            print("Top 5 Season 2022: ")
            print(drivers[:5])
        elif choice == 2:
            print("Last 4 Season 2022: ")
            print(drivers[-4:])
        elif choice == 3:
            print("Drivers in Alphabetical order: ")
            for d in (sorted(drivers)):
                print(d)
        elif choice == 4:
            print(f"Fernando Alonso finished the season in {(drivers.index('Fernando Alonso')+1)}th place.")
        if 0 < choice < 5:
            break
    while True:
        resp = str(input("Would you like to see another option [Y/N]? "))
        if resp in 'YyNn':
            break
    if resp in 'Nn':
        break
print("Thanks for running our program.")
