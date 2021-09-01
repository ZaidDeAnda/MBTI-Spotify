import spotipy
import streamlit as st
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import numpy as np

client_id="e88fcc8e9e7f460282e4e2cc9b1c9816"
client_secret="0b12644ce9ff486187c6c4a595692de6"
redirect_uri="https://example.com/callback"
scope="user-top-read"

ids=[]

def load_user():
	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
	results = sp.current_user_top_tracks(time_range='medium_term')
	return sp, results

if st.button("Carga tu top de canciones"):
	sp, songs = load_user()
	cols=[2]
	cols= st.beta_columns(2)
	for j in range(len(songs['items'])):
		if j%2==0:
			i=0
		else:
			i=1
		cols[i].image(songs['items'][j]['album']['images'][0]['url'])
		cols[i].write(songs['items'][j]['name']+" - "+songs['items'][j]['artists'][0]['name'])
		print(songs['items'][j]['name']+" - "+songs['items'][j]['artists'][0]['name'])

	#for song in songs['items']:
	#	st.write(song['name']+" - "+song['artists'][0]['name']) 
	#	ids.append(song['id'])
	features= sp.audio_features(ids)


 		
