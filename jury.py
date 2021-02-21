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

    def close_votes_seasons():
        close_seasons = []
        for i in range(num_seasons):
            season_num = i + 1
            check_list = [] # who got votes
            clean_list = [] # cleaned list of votes
            votes = {} # dictionary that will track the votes
            vote_list = [] # values of votes
            season_votes = query_db("SELECT Stats.final_vote_id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.season_id = ?;", [season_num])
            for x in range(4):
                for v in season_votes:
                    if v[0] == None:
                        season_votes.remove(v)
            for d in season_votes:
                if d[0] not in check_list:
                    check_list.append(d[0])
            for y in season_votes:
                clean_list.append(y[0])
            for t in check_list:
                votes[t] = 0
            for n in check_list:
                for m in clean_list:
                    if m == n:
                        votes[n] += 1
            for final in votes.values():
                vote_list.append(final)
            vote_list.sort()
            final_count = vote_list[0]
            for vote in vote_list[1:]:
                final_count -= vote
            if final_count > -2 and final_count < 2:
                close_seasons.append(season_num) 
        return close_seasons

    def num_finalists(season):
        season_num = season
        finalists = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.final_contestant = 1 AND Stats.season_id = ?;", [season_num])
        return len(finalists)

    def close_season_contestants(table, column, season, it):
        season_num = season
        finalist = query_db(f"SELECT {table}.{column} FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.final_contestant = 1 AND Stats.season_id = ?;", [season_num])
        return finalist[it][0]

    def tally_votes(season, it, lst):
        season_num = season
        check_list = [] # who got votes
        clean_list = [] # cleaned list of votes
        votes = {} # dictionary that will track the votes
        vote_list = [] # values of votes
        season_votes = query_db("SELECT Stats.final_vote_id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.season_id = ?;", [season_num])
        for x in range(4):
            for v in season_votes:
                if v[0] == None:
                    season_votes.remove(v)
        for d in season_votes:
            if d[0] not in check_list:
                check_list.append(d[0])
        for y in season_votes:
            clean_list.append(y[0])
        for t in check_list:
            votes[t] = 0
        for n in check_list:
            for m in clean_list:
                if m == n:
                    votes[n] += 1 
        finalist = query_db("SELECT Stats.player_id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.final_contestant = 1 AND Stats.season_id = ?;", [season_num])
        id = finalist[it][0]
        players_votes = votes.get(id)
        if players_votes == None:
            return 0
        else: 
            return players_votes

    def make_vote_dict():
        players = query_db("SELECT Stats.player_id, Stats.final_vote_id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id;")
        clean_player_list = []
        unique = 10000
        for item in players:
            if item[1] != None:
                clean_player_list.append(item[0])
        voters = {}
        season = 1
        for cont in clean_player_list:
            check_season = query_db("SELECT Seasons.id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.player_id = ?;", [cont])
            check_season_clean = []
            for item in check_season:
                check_season_clean.append(item[0])
            if season not in check_season_clean:
                season += 1
                continue
            else:
                unique_id = cont
                if unique_id in voters:
                    unique_id += unique
                    unique += 10000
                name = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.player_id = ? AND Stats.season_id = ?;", [cont, season])
                gender = query_db("SELECT Players.gender FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.player_id = ? AND Stats.season_id = ?;", [cont, season])
                vcf = query_db("SELECT Stats.final_vote_id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.player_id = ? AND Stats.season_id = ?;", [cont, season])
                vcf_clean = vcf[0][0]
                vcf_name = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.player_id = ? AND Stats.season_id = ?;", [vcf_clean, season])
                vcf_gender = query_db("SELECT Players.gender FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.player_id = ? AND Stats.season_id = ?;", [vcf_clean, season])
            voters[unique_id] = {'name': name[0][0], 'gender': gender[0][0], 'vote_cast_for_id': vcf_clean, 'vote_cast_for_name': vcf_name, 'vote_cast_for_gender': vcf_gender}
        return voters


        # season = 0
        # inc = 1
        # for cont in clean_player_list:
        #     unique_id = cont
        #     move = 0
        #     if unique_id in voters:
        #         unique_id += unique
        #         unique += 10000
        #         move += inc
        #         inc += 1
        #     season_check = query_db("SELECT Seasons.id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.player_id = ?;", [cont])
            # if season_check[move][0] > season:
            #     season += 1
            # name = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.player_id = ? AND Stats.season_id = ?;", [cont, season])
            # gender = query_db("SELECT Players.gender FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.player_id = ? AND Stats.season_id = ?;", [cont, season])
            # vcf = query_db("SELECT Stats.final_vote_id FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.player_id = ? AND Stats.season_id = ?;", [cont, season])
            # vcf_clean = vcf
            # vcf_name = query_db("SELECT Stats.name FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.player_id = ? AND Stats.season_id = ?;", [vcf_clean, season])
            # vcf_gender = query_db("SELECT Players.gender FROM Stats JOIN Players JOIN Seasons ON Players.id = Stats.player_id AND Stats.season_id = Seasons.id WHERE Stats.player_id = ? AND Stats.season_id = ?;", [vcf_clean, season])
            # voters[unique_id] = {'name': name[0][0], 'gender': gender[0][0], 'vote_cast_for_id': vcf_clean, 'vote_cast_for_name': vcf_name, 'vote_cast_for_gender': vcf_gender}




