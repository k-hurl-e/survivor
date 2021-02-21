from queries import query_db, get_db, DATABASE, num_seasons

class winclass:
    def women_seasons():
        women_seasons = query_db("SELECT Stats.season_id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'W' AND Stats.sole_survivor = 1;")
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
        woman = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'W' AND Stats.sole_survivor = 1 AND season_id = ?;", [it], one=True)
        return woman[0]

    def men_winners(table, column, it):
        man = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'M' AND Stats.sole_survivor = 1 AND season_id = ?;", [it], one=True)
        return man[0]

    def nb_winners(table, column, it):
        man = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'NB' AND Stats.sole_survivor = 1 AND season_id = ?;", [it], one=True)
        return man[0]

    def num_women_winners():
        women_seasons = query_db("SELECT Stats.season_id FROM Stats JOIN Players ON Players.id = Stats.player_id WHERE Players.gender = 'W' AND Stats.sole_survivor = 1;")
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

    def southern_winners(table, column, it):
        #12 states
        winners = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE sole_survivor = 1 AND (Stats.hometown LIKE '%, TX' OR Stats.hometown LIKE '%, OK'  OR Stats.hometown LIKE '%, AR'  OR Stats.hometown LIKE '%, MS' OR Stats.hometown LIKE '%, AL' OR Stats.hometown LIKE '%, TN' OR Stats.hometown LIKE '%, GA' OR Stats.hometown LIKE '%, FL' OR Stats.hometown LIKE '%, SC' OR Stats.hometown LIKE '%, NC' OR Stats.hometown LIKE '%, KY' OR Stats.hometown LIKE '%, LA');")
        return winners[it][0]

    def num_southern_winners():
        #12 states
        winners = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE sole_survivor = 1 AND (Stats.hometown LIKE '%, TX' OR Stats.hometown LIKE '%, OK'  OR Stats.hometown LIKE '%, AR'  OR Stats.hometown LIKE '%, MS' OR Stats.hometown LIKE '%, AL' OR Stats.hometown LIKE '%, TN' OR Stats.hometown LIKE '%, GA' OR Stats.hometown LIKE '%, FL' OR Stats.hometown LIKE '%, SC' OR Stats.hometown LIKE '%, NC' OR Stats.hometown LIKE '%, KY' OR Stats.hometown LIKE '%, LA');")
        return len(winners)

    def midatlantic_winners(table, column, it):
        #7 states plus DC
        winners = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE sole_survivor = 1 AND (Stats.hometown LIKE '%, NY' OR Stats.hometown LIKE '%, NJ'  OR Stats.hometown LIKE '%, PA'  OR Stats.hometown LIKE '%, DE' OR Stats.hometown LIKE '%, MD' OR Stats.hometown LIKE '%, D.C.' OR Stats.hometown LIKE '%, VA' OR Stats.hometown LIKE '%, WV');")
        return winners[it][0]
    
    def num_midatlantic_winners():
        #7 states plus DC
        winners = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE sole_survivor = 1 AND (Stats.hometown LIKE '%, NY' OR Stats.hometown LIKE '%, NJ'  OR Stats.hometown LIKE '%, PA'  OR Stats.hometown LIKE '%, DE' OR Stats.hometown LIKE '%, MD' OR Stats.hometown LIKE '%, D.C.' OR Stats.hometown LIKE '%, VA' OR Stats.hometown LIKE '%, WV');")
        return len(winners)

    def newengland_winners(table, column, it):
        #6 states
        winners = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE sole_survivor = 1 AND (Stats.hometown LIKE '%, CT' OR Stats.hometown LIKE '%, ME'  OR Stats.hometown LIKE '%, MA'  OR Stats.hometown LIKE '%, NH' OR Stats.hometown LIKE '%, RI' OR Stats.hometown LIKE '%, VT');")
        return winners[it][0]

    def num_newengland_winners():
        #6 states
        winners = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE sole_survivor = 1 AND (Stats.hometown LIKE '%, CT' OR Stats.hometown LIKE '%, ME'  OR Stats.hometown LIKE '%, MA'  OR Stats.hometown LIKE '%, NH' OR Stats.hometown LIKE '%, RI' OR Stats.hometown LIKE '%, VT');")
        return len(winners)

    def western_winners(table, column, it):
        #13 states
        winners = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE sole_survivor = 1 AND (Stats.hometown LIKE '%, AL' OR Stats.hometown LIKE '%, NM'  OR Stats.hometown LIKE '%, CO'  OR Stats.hometown LIKE '%, WY' OR Stats.hometown LIKE '%, MT' OR Stats.hometown LIKE '%, AZ' OR Stats.hometown LIKE '%, UT' OR Stats.hometown LIKE '%, ID' OR Stats.hometown LIKE '%, CA' OR Stats.hometown LIKE '%, NV' OR Stats.hometown LIKE '%, OR' OR Stats.hometown LIKE '%, WA' OR Stats.hometown LIKE '%, HI');")
        return winners[it][0]

    def num_western_winners():
        #13 states
        winners = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE sole_survivor = 1 AND (Stats.hometown LIKE '%, AL' OR Stats.hometown LIKE '%, NM'  OR Stats.hometown LIKE '%, CO'  OR Stats.hometown LIKE '%, WY' OR Stats.hometown LIKE '%, MT' OR Stats.hometown LIKE '%, AZ' OR Stats.hometown LIKE '%, UT' OR Stats.hometown LIKE '%, ID' OR Stats.hometown LIKE '%, CA' OR Stats.hometown LIKE '%, NV' OR Stats.hometown LIKE '%, OR' OR Stats.hometown LIKE '%, WA' OR Stats.hometown LIKE '%, HI');")
        return len(winners)

    def midwest_winners(table, column, it):
        #12 states
        winners = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE sole_survivor = 1 AND (Stats.hometown LIKE '%, OH' OR Stats.hometown LIKE '%, MI'  OR Stats.hometown LIKE '%, IN'  OR Stats.hometown LIKE '%, IL' OR Stats.hometown LIKE '%, WI' OR Stats.hometown LIKE '%, MO' OR Stats.hometown LIKE '%, IA' OR Stats.hometown LIKE '%, MN' OR Stats.hometown LIKE '%, KS' OR Stats.hometown LIKE '%, NE' OR Stats.hometown LIKE '%, SD' OR Stats.hometown LIKE '%, ND');")
        return winners[it][0]

    def num_midwest_winners():
        #12 states
        winners = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE sole_survivor = 1 AND (Stats.hometown LIKE '%, OH' OR Stats.hometown LIKE '%, MI'  OR Stats.hometown LIKE '%, IN'  OR Stats.hometown LIKE '%, IL' OR Stats.hometown LIKE '%, WI' OR Stats.hometown LIKE '%, MO' OR Stats.hometown LIKE '%, IA' OR Stats.hometown LIKE '%, MN' OR Stats.hometown LIKE '%, KS' OR Stats.hometown LIKE '%, NE' OR Stats.hometown LIKE '%, SD' OR Stats.hometown LIKE '%, ND');")
        return len(winners)
