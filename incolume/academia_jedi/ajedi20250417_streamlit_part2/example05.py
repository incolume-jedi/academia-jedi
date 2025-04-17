"""Example3 wide."""

# ruff: noqa: PD002 PLR2004
import pandas as pd
import streamlit as st
from incolume.academia_jedi.ajedi20250414_estudos_streamlit import datafile

st.set_page_config(
    layout='wide',
    page_title='Spotify songs',
)
df0 = pd.read_csv(datafile)

st.session_state['df_spotify'] = df0  # cache state

df0.set_index('Track', inplace=True)

artists = df0.Artist.value_counts().index
artist = st.sidebar.selectbox('Artista', artists)
df_filtered = df0[df0.Artist == artist]

albuns = df_filtered.Album.value_counts().index
album = st.selectbox('Album', albuns)
df_filtered2 = df0[df0.Album == album]

# show = st.checkbox('Display graph')
# if show:
#     st.bar_chart(df_filtered2['Stream'])

col1, col2 = st.columns(2)
col1.bar_chart(df_filtered2['Stream'])
col2.line_chart(df_filtered2['Danceability'])

st.write(artist)
col1, col2 = st.columns([.3,.7])
col2.bar_chart(df_filtered2['Stream'])
col1.line_chart(df_filtered2['Danceability'])
