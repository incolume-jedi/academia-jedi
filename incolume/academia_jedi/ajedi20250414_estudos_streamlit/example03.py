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

st.line_chart(df0[df0.Stream > 1_000_000_000]['Stream'])
