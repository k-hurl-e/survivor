import sqlite3
from query.queries import *
from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def home():
    return render_template('home.html', num_seasons=num_seasons, list_winners=list_winners, winner_age=winner_age, winner_towns=winner_towns, season_list=season_list, tribal_wins=tribal_wins, in_wins=in_wins, total_wins=total_wins)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
