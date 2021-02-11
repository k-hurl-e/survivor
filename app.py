import sqlite3
from flask import Flask, render_template, g

app = Flask(__name__)
DATABASE = 'survivor.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# write functions that make the queries you want and then parse them and return strings

@app.route("/")
def home():
    return render_template('home.html', full_name=full_name, bio=bio, reel=reel, twitter=twitter, instagram=instagram, facebook=facebook, imdb=imdb)

if __name__ == '__main__':
    app.run(debug=True)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
