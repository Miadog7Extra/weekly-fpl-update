import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import io

def create_poster(fixtures, managers, standings):
    # Map team IDs to names
    managers_list = managers[0]

    team_id_to_name = {m['team_id']: m['team_name'] for m in managers_list}

    # Create standings table
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('tight')
    ax.axis('off')

    standings_list = standings[0]

    standings_table = [[team_id_to_name[team['team_id']], team['rank'], team['points'], 
                        team['won'], team['draw'], team['lost'], team['points_for'], team['points_against']] 
                       for team in standings_list]
    
    col_labels = ['Team', 'Rank', 'Total Points', 'Won', 'Draw', 'Lost', 'Points for', 'Points against']
    ax.table(cellText=standings_table, colLabels=col_labels, cellLoc='center', loc='center')

    # Save standings table to image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    standings_img = Image.open(buf)

    # Create a blank poster
    poster_width = 800
    poster_height = 1200
    poster = Image.new('RGB', (poster_width, poster_height), (255, 255, 255))

    # Add league title
    draw = ImageDraw.Draw(poster)
    title_font = ImageFont.truetype("arial.ttf", 40)
    draw.text((20, 20), "Theoss Hyttedraft", font=title_font, fill="black")

    # Paste the standings table image onto the poster
    poster.paste(standings_img, (20, 80))

    # Add fixtures
    fixtures_y_position = standings_img.height + 100
    draw.text((20, fixtures_y_position), "Gameweek 1 Fixtures & Results", font=title_font, fill="black")

    fixture_font = ImageFont.truetype("arial.ttf", 24)
    y_offset = fixtures_y_position + 50

    fixtures_list = fixtures[0]

    for fixture in fixtures_list:
        home_team_name = team_id_to_name[fixture['home_team']]
        away_team_name = team_id_to_name[fixture['away_team']]
        fixture_text = f"{home_team_name} {fixture['home_team_points']} - {fixture['away_team_points']} {away_team_name}"
        draw.text((20, y_offset), fixture_text, font=fixture_font, fill="black")
        y_offset += 40

    # Save the final poster image
    poster.save("league_poster.png")