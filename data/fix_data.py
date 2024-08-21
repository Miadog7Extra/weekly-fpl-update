
def generate_team_id_to_name(managers):
    managers_list = managers[0]

    # Map team IDs to names
    team_id_to_name = {m['team_id']: m['team_name'] for m in managers_list}

    return team_id_to_name

def generate_fixtures_html(fixtures, team_id_to_names):
    fixtures_html = ""
    fixtures_list = fixtures[0]
    for fixture in fixtures_list:
        home_team_name = team_id_to_names.get(fixture['home_team'], "Unknown Team")
        away_team_name = team_id_to_names.get(fixture['away_team'], "Unknown Team")
        home_team_points = fixture['home_team_points']
        away_team_points = fixture['away_team_points']
        
        # Generate HTML for each fixture
        fixture_html = f"<p>{home_team_name} {home_team_points} - {away_team_points} {away_team_name}</p>"
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
    standings_list = standings[0]

    for standing in standings_list:
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
    # Replace the placeholder '{{ fixtures }}' in the template with the actual fixtures HTML
    filled_html = html_template.replace("{{ fixtures }}", fixtures_html)
    filled_html = filled_html.replace("{{ table_standings }}", table_html)
    filled_html = filled_html.replace("{{ gamweek_number }}", gameweek_number)
    return filled_html