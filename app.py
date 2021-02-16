import sqlite3
from flask import Flask, render_template, g
from queries import query_db, get_db, DATABASE, num_seasons
import visuals
import winners
import players
import jury

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

def makevisuals():
    with app.app_context():
        visuals.visualmaker.makecroppedpie2('gender_pie_winners', value1=winners.winclass.num_women_winners(), value2=winners.winclass.num_men_winners())
        visuals.visualmaker.makecroppedpie2('gender_pie_players', value1=players.playerclass.num_women_players(), value2=players.playerclass.num_men_players())
        visuals.visualmaker.makeagepie('age_pie_winners', value1=winners.winclass.age_group_winners(20, 29), value2=winners.winclass.age_group_winners(30, 39), value3=winners.winclass.age_group_winners(40, 49), value4=winners.winclass.age_group_winners(50, 100))
        visuals.visualmaker.makeagepie('age_pie_players', value1=players.playerclass.age_group_players(20, 29), value2=players.playerclass.age_group_players(30, 39), value3=players.playerclass.age_group_players(40, 49), value4=players.playerclass.age_group_players(50, 100))
        visuals.visualmaker.makeregionpie('region_pie_players', value1=players.playerclass.num_southern_players() , value2=players.playerclass.num_midatlantic_players() , value3=players.playerclass.num_newengland_players(), value4=players.playerclass.num_western_players(), value5=players.playerclass.num_midwest_players())
        visuals.visualmaker.makeregionpie('region_pie_winners', value1=winners.winclass.num_southern_winners() , value2=winners.winclass.num_midatlantic_winners() , value3=winners.winclass.num_newengland_winners(), value4=winners.winclass.num_western_winners(), value5=winners.winclass.num_midwest_winners())
    return app

makevisuals()

@app.route("/")
def home():
    return render_template('home.html',
    num_seasons=num_seasons,
    winclass=winners.winclass,
    playerclass=players.playerclass,
    juryclass=jury.juryclass)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
