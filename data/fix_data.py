
def generate_team_id_to_name(managers):

    team_id_to_name = {m['team_id']: m['team_name'] for m in managers}

    return team_id_to_name

def generate_fixtures_html(fixtures, team_id_to_names, teams):
    fixtures_html = ""

    for fixture in fixtures:
        home_team_name = team_id_to_names.get(fixture['home_team'], "Unknown Team")
        away_team_name = team_id_to_names.get(fixture['away_team'], "Unknown Team")
        home_team_points = fixture['home_team_points']
        away_team_points = fixture['away_team_points']
        

        fixture_html = "<div class='fixture'>"


        home_team_top_players = sorted(
            teams.get(fixture['home_team'], []), 
            key=lambda x: x['player_points'], 
            reverse=True
        )[:3]

        fixture_html += f"<div class='team'><h3>{home_team_name}</h3><ul>"
        for player in home_team_top_players:
            if player['benched']:
                fixture_html += f"<li style='color: red;'>{player['player_name']}: {player['player_points']} poeng</li>"
            else:
                fixture_html += f"<li>{player['player_name']}: {player['player_points']} poeng</li>"
        fixture_html += "</ul></div>"

        fixture_html += f"<div class='result'><p>{home_team_points} - {away_team_points}</p></div>"


        away_team_top_players = sorted(
            teams.get(fixture['away_team'], []), 
            key=lambda x: x['player_points'], 
            reverse=True
        )[:3]
        
        fixture_html += f"<div class='team'><h3>{away_team_name}</h3><ul>"
        for player in away_team_top_players:
            if player['benched']:
                fixture_html += f"<li style='color: red;'>{player['player_name']}: {player['player_points']} poeng</li>"
            else:
                fixture_html += f"<li>{player['player_name']}: {player['player_points']} poeng</li>"
        fixture_html += "</ul></div>"


        fixture_html += "</div>"

        fixtures_html += fixture_html + "\n"
    
    return fixtures_html

def generate_table_html(standings, team_id_to_names):
    table_html = """
    <table>
        <tr>
            <th>Rank</th>
            <th>Team</th>
            <th>Points</th>
            <th>Won</th>
            <th>Draw</th>
            <th>Lost</th>
            <th>+</th>
            <th>-</th>
        </tr>
    """

    for standing in standings:
        rank = standing['rank']
        team_name = team_id_to_names.get(standing['team_id'], "Unknown Team")
        points = standing['points']
        won = standing['won']
        draw = standing['draw']
        lost = standing['lost']
        points_for = standing['points_for']
        points_against = standing['points_against']

        table_html += f"""
        <tr>
            <td>{rank}</td>
            <td>{team_name}</td>
            <td>{points}</td>
            <td>{won}</td>
            <td>{draw}</td>
            <td>{lost}</td>
            <td>{points_for}</td>
            <td>{points_against}</td>
        </tr>
        """
    table_html += "</table>"


    return table_html

def fill_html_template(html_template, fixtures_html, table_html, gameweek_number):
    filled_html = html_template.replace("{{ fixtures }}", fixtures_html)
    filled_html = filled_html.replace("{{ table_standings }}", table_html)
    filled_html = filled_html.replace("{{ gameweek_number }}", gameweek_number)
    return filled_html