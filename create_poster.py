import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import io

def create_poster_preview(fixtures, managers, standings):
    # Access the first (and only) list inside the managers list

    # Map team IDs to names
    team_id_to_name = {m['team_id']: m['team_name'] for m in managers}

    # Create styled standings table
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('tight')
    ax.axis('off')


    standings_table = [
        [
            team_id_to_name[team['team_id']],
            team['rank'],
            team['points'],
            team['won'],
            team['draw'],
            team['lost'],
            team['points_for'],
            team['points_against']
        ] 
        for team in standings
    ]
    
    col_labels = ['Team', 'Rank', 'Points', 'Won', 'Draw', 'Lost', 'For', 'Against']
    table = ax.table(cellText=standings_table, colLabels=col_labels, cellLoc='center', loc='center')

    # Apply styles to table
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1.2, 1.2)

    for key, cell in table.get_celld().items():
        cell.set_edgecolor('gray')
        if key[0] == 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#4CAF50')  # Header color
        else:
            cell.set_facecolor('#f2f2f2' if key[0] % 2 == 0 else 'white')  # Alternating row colors

    # Save standings table to image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=300)
    buf.seek(0)
    standings_img = Image.open(buf)

    # Create a blank poster with background color
    poster_width = 800
    poster_height = 1200
    poster = Image.new('RGB', (poster_width, poster_height), '#34495E')

    # Add league title with custom font and color
    draw = ImageDraw.Draw(poster)
    title_font = ImageFont.load_default()
    draw.text((50, 30), "Fantasy League Standings", font=title_font, fill="white")

    # Paste the standings table image onto the poster
    poster.paste(standings_img, (50, 120))

    # Add fixtures section with custom styling
    fixtures_y_position = standings_img.height + 150
    draw.text((50, fixtures_y_position), "Gameweek 1 Fixtures & Results", font=title_font, fill="white")

    fixture_font = ImageFont.load_default()
    y_offset = fixtures_y_position + 70

    fixtures_list = fixtures[0]

    for fixture in fixtures_list:
        home_team_name = team_id_to_name[fixture['home_team']]
        away_team_name = team_id_to_name[fixture['away_team']]
        fixture_text = f"{home_team_name} {fixture['home_team_points']} - {fixture['away_team_points']} {away_team_name}"
        draw.text((50, y_offset), fixture_text, font=fixture_font, fill="white")
        y_offset += 50

    # Save the final poster image
    buf = io.BytesIO()
    poster.save(buf, format='png')
    buf.seek(0)
    return Image.open(buf)