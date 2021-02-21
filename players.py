from queries import query_db, get_db, DATABASE, num_seasons

class playerclass:
    def women_players(table, column):
        women_players = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'W';")
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
        women_players = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Players.gender = 'W';")
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

    def southern_players(table, column, it):
        #12 states
        players = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE (Stats.hometown LIKE '%, TX' OR Stats.hometown LIKE '%, OK'  OR Stats.hometown LIKE '%, AR'  OR Stats.hometown LIKE '%, MS' OR Stats.hometown LIKE '%, AL' OR Stats.hometown LIKE '%, TN' OR Stats.hometown LIKE '%, GA' OR Stats.hometown LIKE '%, FL' OR Stats.hometown LIKE '%, SC' OR Stats.hometown LIKE '%, NC' OR Stats.hometown LIKE '%, KY' OR Stats.hometown LIKE '%, LA');")
        return players[it][0]

    def num_southern_players():
        #12 states
        players = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE (Stats.hometown LIKE '%, TX' OR Stats.hometown LIKE '%, OK'  OR Stats.hometown LIKE '%, AR'  OR Stats.hometown LIKE '%, MS' OR Stats.hometown LIKE '%, AL' OR Stats.hometown LIKE '%, TN' OR Stats.hometown LIKE '%, GA' OR Stats.hometown LIKE '%, FL' OR Stats.hometown LIKE '%, SC' OR Stats.hometown LIKE '%, NC' OR Stats.hometown LIKE '%, KY' OR Stats.hometown LIKE '%, LA');")
        return len(players)

    def midatlantic_players(table, column, it):
        #7 states plus DC
        players = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE (Stats.hometown LIKE '%, NY' OR Stats.hometown LIKE '%, NJ'  OR Stats.hometown LIKE '%, PA'  OR Stats.hometown LIKE '%, DE' OR Stats.hometown LIKE '%, MD' OR Stats.hometown LIKE '%, D.C.' OR Stats.hometown LIKE '%, VA' OR Stats.hometown LIKE '%, WV');")
        return players[it][0]
    
    def num_midatlantic_players():
        #7 states plus DC
        players = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE (Stats.hometown LIKE '%, NY' OR Stats.hometown LIKE '%, NJ'  OR Stats.hometown LIKE '%, PA'  OR Stats.hometown LIKE '%, DE' OR Stats.hometown LIKE '%, MD' OR Stats.hometown LIKE '%, D.C.' OR Stats.hometown LIKE '%, VA' OR Stats.hometown LIKE '%, WV');")
        return len(players)

    def newengland_players(table, column, it):
        #6 states
        players = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE (Stats.hometown LIKE '%, CT' OR Stats.hometown LIKE '%, ME'  OR Stats.hometown LIKE '%, MA'  OR Stats.hometown LIKE '%, NH' OR Stats.hometown LIKE '%, RI' OR Stats.hometown LIKE '%, VT');")
        return players[it][0]

    def num_newengland_players():
        #6 states
        players = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE (Stats.hometown LIKE '%, CT' OR Stats.hometown LIKE '%, ME'  OR Stats.hometown LIKE '%, MA'  OR Stats.hometown LIKE '%, NH' OR Stats.hometown LIKE '%, RI' OR Stats.hometown LIKE '%, VT');")
        return len(players)

    def western_players(table, column, it):
        #13 states
        players = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE (Stats.hometown LIKE '%, AL' OR Stats.hometown LIKE '%, NM'  OR Stats.hometown LIKE '%, CO'  OR Stats.hometown LIKE '%, WY' OR Stats.hometown LIKE '%, MT' OR Stats.hometown LIKE '%, AZ' OR Stats.hometown LIKE '%, UT' OR Stats.hometown LIKE '%, ID' OR Stats.hometown LIKE '%, CA' OR Stats.hometown LIKE '%, NV' OR Stats.hometown LIKE '%, OR' OR Stats.hometown LIKE '%, WA' OR Stats.hometown LIKE '%, HI');")
        return players[it][0]

    def num_western_players():
        #13 states
        players = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE (Stats.hometown LIKE '%, AL' OR Stats.hometown LIKE '%, NM'  OR Stats.hometown LIKE '%, CO'  OR Stats.hometown LIKE '%, WY' OR Stats.hometown LIKE '%, MT' OR Stats.hometown LIKE '%, AZ' OR Stats.hometown LIKE '%, UT' OR Stats.hometown LIKE '%, ID' OR Stats.hometown LIKE '%, CA' OR Stats.hometown LIKE '%, NV' OR Stats.hometown LIKE '%, OR' OR Stats.hometown LIKE '%, WA' OR Stats.hometown LIKE '%, HI');")
        return len(players)

    def midhwest_players(table, column, it):
        #12 states
        players = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE (Stats.hometown LIKE '%, OH' OR Stats.hometown LIKE '%, MI'  OR Stats.hometown LIKE '%, IN'  OR Stats.hometown LIKE '%, IL' OR Stats.hometown LIKE '%, WI' OR Stats.hometown LIKE '%, MO' OR Stats.hometown LIKE '%, IA' OR Stats.hometown LIKE '%, MN' OR Stats.hometown LIKE '%, KS' OR Stats.hometown LIKE '%, NE' OR Stats.hometown LIKE '%, SD' OR Stats.hometown LIKE '%, ND');")
        return players[it][0]

    def num_midwest_players():
        #12 states
        players = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE (Stats.hometown LIKE '%, OH' OR Stats.hometown LIKE '%, MI'  OR Stats.hometown LIKE '%, IN'  OR Stats.hometown LIKE '%, IL' OR Stats.hometown LIKE '%, WI' OR Stats.hometown LIKE '%, MO' OR Stats.hometown LIKE '%, IA' OR Stats.hometown LIKE '%, MN' OR Stats.hometown LIKE '%, KS' OR Stats.hometown LIKE '%, NE' OR Stats.hometown LIKE '%, SD' OR Stats.hometown LIKE '%, ND');")
        return len(players)

    def all_player_ids():
        players = query_db("SELECT Stats.player_id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id;")
        clean_player_list = []
        for item in players:
            clean_player_list.append(item[0])
        return clean_player_list
