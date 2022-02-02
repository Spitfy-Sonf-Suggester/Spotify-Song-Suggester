import pandas as pd
import numpy as np
import os

path = os.path.join(os.getcwd(), 'data.csv')
df = pd.read_csv(path)
df = df[['name', 'acousticness', 'danceability', 'energy', 'loudness',
                 'mode', 'liveness', 'valence', 'tempo', 'duration_ms']]


# name = DB.Column(DB.String(70), primary_key=True, nullable=False)
#     c_code = DB.Column(DB.String, nullable=False)
#     continent = DB.Column(DB.String, nullable=False)
#     population = DB.Column(DB.Float, nullable=False)
# class Song(DB.Model):

#     id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
#     name = DB.Column(DB.String(50), nullable=False)
#     acoustic = DB.Column(DB.Float, nullable=False)
#     danceable = DB.Column(DB.Float, nullable=False)
#     energy = DB.Column(DB.Float, nullable=False)
#     loudness = DB.Column(DB.Float, nullable=False)
#     mode = DB.Column(DB.Float, nullable=False)
#     liveness = DB.Column(DB.Float, nullable=False)
#     valence = DB.Column(DB.Float, nullable=False)
#     tempo = DB.Column(DB.Float, nullable=False)
#     duration_ms = DB.Column(DB.Float, nullable=False)

#     def __repr__(self):
#         return f'{self.name} is {round(self.duration_ms*60000, 2)} minutes long'




