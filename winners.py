from queries import query_db, get_db, DATABASE, num_seasons

class winclass:
    def women_seasons():
        women_seasons = query_db("SELECT Stats.season_id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'F' AND Stats.sole_survivor = 1;")
        women_seasons_cleaned = []
        for x in range(len(women_seasons)):
            women_seasons_cleaned.append(women_seasons[x][0])
        women_seasons_cleaned.sort()
        return women_seasons_cleaned

    def men_seasons():
        men_seasons = query_db("SELECT Stats.season_id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'M' AND Stats.sole_survivor = 1;")
        men_seasons_cleaned = []
        for x in range(len(men_seasons)):
            men_seasons_cleaned.append(men_seasons[x][0])
        men_seasons_cleaned.sort()
        return men_seasons_cleaned

    def nb_seasons():
        nb_seasons = query_db("SELECT Stats.season_id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'NB' AND Stats.sole_survivor = 1;")
        nb_seasons_cleaned = []
        for x in range(len(nb_seasons)):
            men_seasons_cleaned.append(nb_seasons[x][0])
        nb_seasons_cleaned.sort()
        return nb_seasons_cleaned

    def ask_winners(table, column, it):
        winner = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.sole_survivor = 1 AND season_id = ?;", [it + 1], one=True)
        return winner[0]

    def women_winners(table, column, it):
        woman = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'F' AND Stats.sole_survivor = 1 AND season_id = ?;", [it], one=True)
        return woman[0]

    def men_winners(table, column, it):
        man = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'M' AND Stats.sole_survivor = 1 AND season_id = ?;", [it], one=True)
        return man[0]

    def nb_winners(table, column, it):
        man = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'NB' AND Stats.sole_survivor = 1 AND season_id = ?;", [it], one=True)
        return man[0]

    def num_women_winners():
        women_seasons = query_db("SELECT Stats.season_id FROM Stats JOIN Players ON Players.id = Stats.player_id WHERE Players.gender = 'F' AND Stats.sole_survivor = 1;")
        women_seasons_cleaned = []
        for x in range(len(women_seasons)):
            women_seasons_cleaned.append(women_seasons[x][0])
        women_seasons_cleaned.sort()
        return len(women_seasons_cleaned)

    def num_men_winners():
        men_seasons = query_db("SELECT Stats.season_id FROM Stats JOIN Players ON Players.id = Stats.player_id WHERE Players.gender = 'M' AND Stats.sole_survivor = 1;")
        men_seasons_cleaned = []
        for x in range(len(men_seasons)):
            men_seasons_cleaned.append(men_seasons[x][0])
        men_seasons_cleaned.sort()
        return len(men_seasons_cleaned)

    def num_nb_winners():
        nb_seasons = query_db("SELECT Stats.season_id FROM Stats JOIN Players ON Players.id = Stats.player_id WHERE Players.gender = 'NB' AND Stats.sole_survivor = 1;")
        nb_seasons_cleaned = []
        for x in range(len(nb_seasons)):
            men_seasons_cleaned.append(nb_seasons[x][0])
        nb_seasons_cleaned.sort()
        return len(nb_seasons_cleaned)

    def oldest_winners(table, column, num, it):
        winner = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.sole_survivor = 1 ORDER BY Stats.age_time_of_filming DESC LIMIT ?;", [num])
        return winner[it][0]

    def youngest_winners(table, column, num, it):
        winner = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.sole_survivor = 1 ORDER BY Stats.age_time_of_filming LIMIT ?;", [num])
        return winner[it][0]

    def age_group_winners(low, high):
        age_group = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.sole_survivor = 1 AND Stats.age_time_of_filming >= ? AND Stats.age_time_of_filming <= ? ORDER BY Stats.age_time_of_filming;", [low, high])
        return len(age_group)
