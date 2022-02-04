import pandas as pd
import numpy as np
import os
import pickle
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

path = os.path.join(os.getcwd(), 'data.csv')
df1 = pd.read_csv(path)
df = df1[['name', 'acousticness', 'danceability', 'energy', 'loudness',
                 'mode', 'liveness', 'valence', 'tempo', 'duration_ms']]
# df_copy = pd.DataFrame({x: df[x][:50000] for x in df.columns if not x == 'name'})

# model = NearestNeighbors(n_neighbors=2, algorithm='brute')
# scaler = StandardScaler()
# feats = scaler.fit_transform(df_copy)
# model.fit(feats)

# with open('my_model.h5', 'wb') as f:
#     pickle.dump(model, f)




