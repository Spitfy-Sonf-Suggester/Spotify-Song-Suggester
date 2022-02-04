from .data import df
from flask import Flask, render_template
import sqlite3
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()
class Song(DB.Model):

    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    name = DB.Column(DB.String(50), nullable=False)
    acoustic = DB.Column(DB.Float, nullable=False)
    danceable = DB.Column(DB.Float, nullable=False)
    energy = DB.Column(DB.Float, nullable=False)
    loudness = DB.Column(DB.Float, nullable=False)
    mode = DB.Column(DB.Float, nullable=False)
    liveness = DB.Column(DB.Float, nullable=False)
    valence = DB.Column(DB.Float, nullable=False)
    tempo = DB.Column(DB.Float, nullable=False)
    duration_ms = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f'{self.name} is {round(self.duration_ms*60000, 2)} minutes long'

'''
suggest a song to the user based on the querying song(i.e. a song the user
just listened to, or a song the user has indicated they enjoy).
'''

def create_app():
    APP = Flask(__name__)
    APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_spotify.sqlite3'
    APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(APP)

    @APP.before_first_request
    def create_tables():
        DB.create_all()

    @APP.route('/')
    def root():
        return render_template('base.html', title='Home', str([(b.name, b.energy) for b in Song.query.all()]))
    
    @APP.route('/refresh')
    def refresh():
        DB.drop_all()
        DB.create_all()
        return 'Data has been refreshed.'

    @APP.route('/add')
    def add_one():

        for x in range(100):
            n, a, d, e, l, m, li, v, t, d = df.iloc[x].values
            temp = Song(id=x, name=n, acoustic=a, danceable=d, energy=e, loudness=l, mode=m, liveness=li, valence=v, tempo=t, duration_ms=d)
            if not Song.query.get(temp.id):
                DB.session.add(temp)
                        
        DB.session.commit()
        return 'Names have been added'
    return APP
