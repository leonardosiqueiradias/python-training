# 5. Classificação de Times de Futebol
# Crie uma tupla contendo os 10 primeiros colocados de um campeonato de
# futebol. Depois, exiba:
# • Os três primeiros colocados.
# • Os últimos três colocados.
# • Os times em ordem alfabética.
# • A posição de um time específico informado pelo usuário.

teams = ('Flamengo', 'Palmeiras', 'Atlético-MG', 'São Paulo', 'Fluminense',
         'Internacional', 'Grêmio', 'Corinthians', 'Santos', 'Athletico-PR')

print(f'The top 3 teams: {teams[:3]}')

print(f'The bottom 3 teams: {teams[-3:]}')

print(f'Teams in alphabetical order: {sorted(teams)}')

team_to_find = input('Enter the name of a team to find its position: ')
if team_to_find in teams:
    print(f'The team {team_to_find} is in position {teams.index(team_to_find) + 1}.')
else:
    print('Team not found in the top 10 rankings.')