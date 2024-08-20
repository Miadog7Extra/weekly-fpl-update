import requests

def get_team_motm(team_id, event_number):
    base_url = 'https://draft.premierleague.com/api/' 


    r = requests.get(base_url+f'entry/{team_id}/event/{event_number}').json()
    
    

get_team_motm(481825, 1)

