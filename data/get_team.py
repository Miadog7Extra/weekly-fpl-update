import requests

def get_team_top_players(team_id, gamweek_number):
    base_url = 'https://draft.premierleague.com/api/' 


    r = requests.get(base_url+f'entry/{team_id}/event/{gamweek_number}/').json()

    print(base_url + f'entry/{team_id}/event/{gamweek_number}/')

    players = []
    players.append({'team_id': team_id})

    for entry in r["picks"]:
        player_id = entry['element']
        player_position = entry["position"]
        players.append({'player_id': player_id, 'player_position': player_position, 'benched': False, 'player_points': 0, 'player_name': 'unknown'})
    
    for player in players:
        if player["player_position"] > 11:
            player.update({'benched': True})
    
    get_player_names(players, gamweek_number)
    
    return players
    
def get_player_names(players, gameweek_number):
    r = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/').json()

    for player in players:
        id = player['player_id']
        for entry in r['elements']:
            if id == entry['id']:
                player_name = entry['web_name']
                player.update({'player_name': player_name})
    
    get_player_points(players, gameweek_number)

    return players

def get_player_points(players, gameweek_number):

    fixtures = get_gameweek_fixtures(gameweek_number)

    for player in players:
        id = player['player_id']
        r = requests.get(f'https://fantasy.premierleague.com/api/element-summary/{id}/').json()
        
        for entry in r['history']:
            if entry['fixture'] in fixtures:
                player_points = entry['total_points']
                player.update({'player_points': player_points}) 
    
    return players


def get_gameweek_fixtures(gameweek):
    r = requests.get('https://fantasy.premierleague.com/api/fixtures/').json()

    gameweek_fixtures = [fixture for fixture in r if fixture['event'] == gameweek]

    fixture_ids = [fixture['id'] for fixture in gameweek_fixtures]

    return fixture_ids

#print(get_team_top_players(481825, 1))

#print(get_gameweek_fixtures(1))
