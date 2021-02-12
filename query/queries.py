import sqlite3
from flask import g

DATABASE = 'survivor.db'
num_seasons = 40

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

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
