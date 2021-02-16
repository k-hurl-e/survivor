from queries import query_db, get_db, DATABASE, num_seasons

class juryclass:
    def unanimous_seasons():
        unanimous_seasons = []
        for i in range(num_seasons):
            season_num = i + 1
            check_list = []
            season_votes = query_db("SELECT Stats.final_vote_id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.season_id = ?;", [season_num])
            for x in range(4):
                for v in season_votes:
                    if v[0] == None:
                        season_votes.remove(v)
            for y in season_votes:
                if y[0] not in check_list:
                    check_list.append(y[0])
            if len(check_list) == 1:
                unanimous_seasons.append(season_num)
        return unanimous_seasons

    def unanimous_winner(table, column, it):
        winner = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.sole_survivor = 1 AND Stats.season_id = ?;", [it], one=True)
        return winner[0]

    