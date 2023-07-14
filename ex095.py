'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.
'''
players = list()
stats = dict()
games = list()
while True:
    stats.clear()
    stats['Name'] = str(input("Player's name: "))
    matches = int(input("Games Played: "))
    games.clear()
    if matches > 0:
        for g in range(0, matches):
            games.append(int(input(f'Gols scored in the #{g+1} game: ')))
    stats['Goals'] = games[:]
    stats["Total"] = sum(games)
    players.append(stats.copy())
    while True:
        resp = str(input('Would you like to register another player [Y/N]?')).strip().upper()[0]
        if resp in 'YN':
            break
    if resp == 'N':
        break
print('~='*30)
print('cod', end='')
for i in stats.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for key, value in enumerate(players):
    print(f'{key:>3}', end='')
    for d in value.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    search = int(input("Would you like to see the stats of which player? (999 to stop) "))
    if search == 999:
        break
    if search >= len(players):
        print('Error! Player not found.')
    else:
        print(f' -- PLAYER STATUS: {players[search]["Name"]}:')
        for i, g in enumerate(players[search]["Goals"]):
            print(f'  On the #{i+1} match, he scored {g} goals.')
print('-'*40)
print(' >>> END OF PROGRAM <<<')
