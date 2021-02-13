import sqlite3
from flask import Flask, render_template, g
from queries import query_db, get_db, DATABASE, num_seasons
import winners

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def home():
    return render_template('home.html', num_seasons=num_seasons, list_winners=winners.winclass.list_winners, winner_age=winners.winclass.winner_age, winner_towns=winners.winclass.winner_towns, season_list=winners.winclass.season_list, tribal_wins=winners.winclass.tribal_wins, in_wins=winners.winclass.in_wins, total_wins=winners.winclass.total_wins)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
