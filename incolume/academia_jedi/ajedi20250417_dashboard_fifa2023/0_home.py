"""Bashboard FIFA 2023."""
# ruff: noqa: N999

import datetime as dt
import webbrowser

import pandas as pd
import streamlit as st
from config import settings
from incolume.academia_jedi.ajedi20250417_dashboard_fifa2023 import (
    URLS,
    get_dataset,
)
from pytz import timezone


@st.cache_data
def load_data() -> bool:
    """Carga de dados."""
    df_data = pd.read_csv(get_dataset(), index_col=0)
    df_data = df_data[
        df_data['Contract Valid Until']
        >= dt.datetime.now(tz=timezone(settings.TZ)).year
    ]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data
    return True


if 'data' not in st.session_state:
    load_data()


st.markdown('# FIFA 2023 OFFICIAL DATASET :soccer: ')
st.sidebar.markdown(
    'Desenvolvido pela _ [Academia JEDI](#)'
    ' - _**A**cademia da **J**unta **E**specializada de'
    ' **D**esenvolvimento e **I**novação',
)

btn = st.button('Acesse os dados no Kaggle')

if btn:
    webbrowser.open_new_tab(URLS.kaggle)

st.markdown(
    'O conjunto de dados de jogaores de futebol de 2017 a 2023'
    ' fornece informações abrangentes sobre jogadores de futebol'
    ' profissionais.'
    'O conjunto de dados contém uma ampla gama de atributos,'
    ' incluindo dados demográficos do jogador, características'
    ' físicas, estatísticas de jogo, detalhes do contrato e'
    ' afiliações de clubes.'
    '\n\n'
    'Com **mas de 17.000 resgitros**, este conjunto de dados oferece'
    ' um recurso valioso para analistas de futebol, pesquisadores e'
    ' entusiastas interessados em explorar vários aspectos do mundo'
    ' do futebol, pois permite estudar, atributos de jogaores, vétricas'
    ' de desempenho, avalidação de mercado, análise de clubes,'
    ' posicionamento de jogadores e desenvolvimento do jogador'
    ' ao longo do tempo.',
)
