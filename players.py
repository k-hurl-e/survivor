from queries import query_db, get_db, DATABASE, num_seasons

class playerclass:
    def women_players(table, column):
        women_players = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'F';")
        women_players_cleaned = []
        for x in range(len(women_players)):
            women_seasons_cleaned.append(women_players[x][0])
        women_players_cleaned.sort()
        return women_players_cleaned

    def men_players(table, column):
        men_players = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'M';")
        men_players_cleaned = []
        for x in range(len(men_players)):
            men_players_cleaned.append(men_players[x][0])
        men_players_cleaned.sort()
        return men_players_cleaned

    def nb_players(table, column):
        nb_players = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'NB';")
        nb_players_cleaned = []
        for x in range(len(nb_players)):
            men_seasons_cleaned.append(nb_players[x][0])
        nb_players_cleaned.sort()
        return nb_players_cleaned

    def num_women_players():
        women_players = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'F';")
        women_players_cleaned = []
        for x in range(len(women_players)):
            women_players_cleaned.append(women_players[x][0])
        return len(women_players_cleaned)

    def num_men_players():
        men_players = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'M';")
        men_players_cleaned = []
        for x in range(len(men_players)):
            men_players_cleaned.append(men_players[x][0])
        return len(men_players_cleaned)

    def num_nb_players():
        nb_players = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'NB';")
        nb_players_cleaned = []
        for x in range(len(nb_players)):
            men_seasons_cleaned.append(nb_players[x][0])
        return len(nb_players_cleaned)

    def age_group_players(low, high):
        age_group = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.age_time_of_filming >= ? AND Stats.age_time_of_filming <= ? ORDER BY Stats.age_time_of_filming;", [low, high])
        return len(age_group)
