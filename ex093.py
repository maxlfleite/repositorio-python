'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
stats = dict()
games = list()
stats['Name'] = str(input("Player's name: "))
matches = int(input("Games Played: "))
if matches > 0:
    for g in range(0, matches):
        games.append(int(input(f'Gols scored in the #{g+1} game: ')))
stats['Goals'] = games[:]
stats["Total"] = sum(games)
print('~='*30)
print(stats)
for k, v in stats.items():
    print(f'The field {k} has {v} in it.')
print('~='*30)
print(f'The player {stats["Name"]} played in {len(stats["Goals"])} matches.')
for i, v in enumerate(stats["Goals"]):
    print(f'   => On the #{i+1} match, he scored {v} goals.')
print(f'A total of {stats["Total"]} goals in the season.')


