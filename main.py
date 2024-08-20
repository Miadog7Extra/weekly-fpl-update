from data.get_details import get_managers, get_gameweek_fixtures, get_standings
from create_poster import create_poster

def main():

    fixtures = [get_gameweek_fixtures(108434, 1)]
    managers = [get_managers(108434)]
    standings = [get_standings(108434)]

    create_poster(fixtures, managers, standings)





if __name__ == '__main__':
    main()