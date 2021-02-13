from queries import query_db, get_db, DATABASE, num_seasons

class winclass:
    def list_winners(it):
        name = query_db('SELECT name FROM Stats WHERE sole_survivor = 1 AND season_id = ?', [(it + 1)], one=True)
        if name is None:
            return 'No such user'
        else:
            return (name[0])

    def winner_age(it):
        age = query_db('SELECT age_time_of_filming FROM Stats WHERE sole_survivor = 1 AND season_id = ?', [(it + 1)], one=True)
        if age is None:
            return 'No such user'
        else:
            return (age[0])

    def winner_towns(it):
        town = query_db('SELECT hometown FROM Stats WHERE sole_survivor = 1 AND season_id = ?', [(it + 1)], one=True)
        if town is None:
            return 'No such user'
        else:
            return (town[0])

    def season_list(it):
        season = query_db('SELECT season FROM Seasons WHERE id = ?', [(it + 1)], one=True)
        if season is None:
            return 'No such user'
        else:
            return (season[0])

    def tribal_wins(it):
        t_wins = query_db('SELECT tribal_wins FROM Stats WHERE sole_survivor = 1 AND season_id = ?', [(it + 1)], one=True)
        if t_wins is None:
            return 'No such user'
        else:
            return (t_wins[0])

    def in_wins(it):
        i_wins = query_db('SELECT individual_wins FROM Stats WHERE sole_survivor = 1 AND season_id = ?', [(it + 1)], one=True)
        if i_wins is None:
            return 'No such user'
        else:
            return (i_wins[0])

    def total_wins(it):
        tot_wins = query_db('SELECT total_wins FROM Stats WHERE sole_survivor = 1 AND season_id = ?', [(it + 1)], one=True)
        if tot_wins is None:
            return 'No such user'
        else:
            return (tot_wins[0])

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
