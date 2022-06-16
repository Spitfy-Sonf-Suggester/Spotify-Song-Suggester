from .data import df, df1
from flask import Flask, render_template, request
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import pickle
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler


from .data import df
from flask import Flask, render_template, request
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
# app factory
def create_app():
    # instantiate app
    APP = Flask(__name__)
    APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_spotify.sqlite3'
    APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # initializing app
    DB.init_app(APP)
    # create tables
    @APP.before_first_request
    def create_tables():
        DB.create_all()

    @APP.route('/', methods=['GET', 'POST'])
    def root():
        if request.method == 'POST':
            # Get form data
            id = request.form.get('search')
            
            try:
                # select matching row from dataframe
                query = df1[df1['id'] == id]
                
                query = query[['acousticness', 'danceability', 'energy', 'loudness',
                    'mode', 'liveness', 'valence', 'tempo', 'duration_ms']].iloc[0].values
                model = pickle.load(
                    open('my_model.h5', 'rb')
                )
                # query = scaler.fit_transform(query)
                distances, indices = model.kneighbors([query])
                # names of 6 nearest neighboring songs
                result = [df.iloc[x]['name'] for x in indices]
                result = ' '.join(map(str, result))
                return render_template('results.html', answer=result)

            # in case the user entry is invalid
            except:
                return render_template('base.html')
            
    
        # route for wiping the database clean

        return render_template('base.html', content=str([(b.name, b.energy) for b in Song.query.all()]), title='Home')

    

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
        # commit changes to database session
        DB.session.commit()
        return 'Names have been added'
    return APP
