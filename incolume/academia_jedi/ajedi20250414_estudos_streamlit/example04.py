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
df0.set_index('Track', inplace=True)

artists = df0.Artist.value_counts().index
artist = st.selectbox('Artista', artists)

df_filtered = df0[df0.Artist == artist]

st.bar_chart(df_filtered['Stream'])

st.write(artist)
