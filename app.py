import sqlite3
from flask import Flask, render_template, g
from queries import query_db, get_db, DATABASE, num_seasons
import winners
import players

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def home():
    return render_template('home.html',
    num_seasons=num_seasons,
    winclass=winners.winclass,
    playerclass=players.playerclass)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
