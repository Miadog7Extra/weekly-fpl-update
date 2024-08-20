import requests


base_url = 'https://draft.premierleague.com/api/' 

def get_managers(league_id):
    r = requests.get(base_url+f'league/{league_id}/details').json()

    managers = []
    for entry in r['league_entries']:
        manager_name = f"{entry['player_first_name']} {entry['player_last_name']}"
        team_name = entry['entry_name']
        team_id = entry['id']
        managers.append({'manager': manager_name, 'team_name': team_name, 'team_id': team_id})

    return managers

def get_gameweek_fixtures(league_id, gameweek_number):
    r = requests.get(base_url+f'league/{league_id}/details').json()

    gameweek = []

    gameweek_found = False

    for entry in r['matches']:

        if entry['event'] == gameweek_number:
            gameweek_found = True

            home_team = entry['league_entry_1']
            home_team_points = entry['league_entry_1_points']

            away_team = entry['league_entry_2']
            away_team_points = entry['league_entry_2_points']
            
            gameweek.append({'home_team': home_team, 'home_team_points': home_team_points, 'away_team': away_team, 'away_team_points': away_team_points})

    if not gameweek_found:
        raise Exception(f'No gameweek numbered {gameweek_number}')
    
    return gameweek

def get_standings(league_id):
    r = requests.get(base_url+f'league/{league_id}/details').json()

    standings = []

    for entry in r['standings']:
        team_id = entry['league_entry']
        rank = entry['rank']
        won = entry['matches_won']
        draw = entry['matches_drawn']
        lost = entry['matches_lost']
        total_points = entry['total']
        points_for = entry['points_for']
        points_against = entry['points_against']

        standings.append({'team_id': team_id, 'rank': rank, 'points': total_points, 'won': won, 'draw': draw, 'lost': lost, 'points_for': points_for, 'points_against': points_against})

    return standings


get_managers(108434)
get_gameweek_fixtures(108434, 1)
get_standings(108434)