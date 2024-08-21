from data.get_details import get_managers, get_gameweek_fixtures, get_standings
from data.fix_data import generate_team_id_to_name, generate_fixtures_html, generate_table_html, fill_html_template

def main():

    gameweek_number = 1
    league_code = 108434

    fixtures = [get_gameweek_fixtures(league_code, gameweek_number)]
    managers = [get_managers(league_code)]
    standings = [get_standings(league_code)]

    team_id_to_names = generate_team_id_to_name(managers)

    fixtures_html = generate_fixtures_html(fixtures, team_id_to_names)
    table_html = generate_table_html(standings, team_id_to_names)

    with open('html_content.html', 'r') as html_file:
        html_template = html_file.read()

    filled_html = fill_html_template(html_template, fixtures_html, table_html, gameweek_number=str(gameweek_number))

    with open(f'gameweek_posters/gameweek-{str(gameweek_number)}.html', 'w') as file:
        file.write(filled_html)


if __name__ == '__main__':
    main()