"""Example1."""
# ruff: noqa: B018, PD002

import pandas as pd
from incolume.academia_jedi.ajedi20250414_estudos_streamlit import datafile

df0 = pd.read_csv(datafile)
df0.set_index('Artist', inplace=True)

df0
