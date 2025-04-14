"""Estudos com streamlit."""

from pathlib import Path

import pandas as pd
import streamlit as st

datafile = (
    Path(__file__).parents[3].joinpath('data_files', 'csv', '01Spotify.csv')
)
df0 = pd.read_csv(datafile)

st.set_page_config(
    layout='wide',
    page_title='spotify songs',
)

# st.write(df0[df0.Stream > 1_000_000_000])

# df0 = df0.set_index('Artist', drop=True)
# st.line_chart(df0[df0.Stream > 1_000_000_000]['Stream'])

df0 = df0.set_index('Track')
st.write(df0)
artists = df0['Artist'].value_counts().index
artist = st.selectbox('Artista', artists)
df_filtered = df0[df0.Artist == artist]

display = st.checkbox('display graph')
if display:
    st.bar_chart(df_filtered['Stream'])

st.write(artist)
# st.write(f'{df0.loc[df0.Artist==artist, 'Track']}')  #
