"""Model dash."""

import dash
import pandas as pd
import plotly.express as px

__all__ = ['px', 'pd']

app = dash.Dash(__name__)

estados_brasileiros = [
    {'label': 'Acre', 'value': 'AC'},
    {'label': 'Alagoas', 'value': 'AL'},
    {'label': 'Amapá', 'value': 'AP'},
    {'label': 'Amazonas', 'value': 'AM'},
    {'label': 'Bahia', 'value': 'BA'},
    {'label': 'Ceará', 'value': 'CE'},
    {'label': 'Distrito Federal', 'value': 'DF'},
    {'label': 'Espírito Santo', 'value': 'ES'},
    {'label': 'Goiás', 'value': 'GO'},
    {'label': 'Maranhão', 'value': 'MA'},
    {'label': 'Mato Grosso', 'value': 'MT'},
    {'label': 'Mato Grosso do Sul', 'value': 'MS'},
    {'label': 'Minas Gerais', 'value': 'MG'},
    {'label': 'Pará', 'value': 'PA'},
    {'label': 'Paraíba', 'value': 'PB'},
    {'label': 'Paraná', 'value': 'PR'},
    {'label': 'Pernambuco', 'value': 'PE'},
    {'label': 'Piauí', 'value': 'PI'},
    {'label': 'Rio de Janeiro', 'value': 'RJ'},
    {'label': 'Rio Grande do Norte', 'value': 'RN'},
    {'label': 'Rio Grande do Sul', 'value': 'RS'},
    {'label': 'Rondônia', 'value': 'RO'},
    {'label': 'Roraima', 'value': 'RR'},
    {'label': 'Santa Catarina', 'value': 'SC'},
    {'label': 'São Paulo', 'value': 'SP'},
    {'label': 'Sergipe', 'value': 'SE'},
    {'label': 'Tocantins', 'value': 'TO'},
]

app.layout = dash.html.Div(
    [
        dash.html.Label('Dropdown'),
        dash.dcc.Dropdown(
            id='dp1',
            options=estados_brasileiros,
            value='DF',
            style={'margin-top': '20px'},
        ),
        dash.html.Label('Checklist', style={'margin-top': '20px'}),
        dash.dcc.Checklist(
            id='cl1',
            options=estados_brasileiros,
            value=['DF'],
            style={'margin-top': '20px'},
        ),
        dash.html.Label('Text input', style={'margin-top': '20px'}),
        dash.dcc.Input(
            id='input1',
            type='text',
            value='Hello Dash',
            style={'margin-top': '20px'},
        ),
        dash.html.Label('Slider', style={'margin-top': '20px'}),
        dash.dcc.Slider(
            id='slider1',
            min=0,
            max=10,
            step=0.1,
            value=5,
            marks={i: str(i) for i in range(11)},
        ),
    ],
)

if __name__ == '__main__':
    app.run(debug=True, port=8052)
