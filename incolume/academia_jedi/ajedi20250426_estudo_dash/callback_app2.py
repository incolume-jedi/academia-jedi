"""Estudo com pacote dash."""

import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output

# Dash app com Figure e Slider

df0 = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv',
)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df0['year'].min(),
        max=df0['year'].max(),
        value=df0['year'].min(),
        marks={str(year): str(year) for year in df0['year'].unique()},
        step=None,
    ),
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')],
)
def update_figure(selected_year):
    """Update figure."""
    filtered_df = df0[df0.year == selected_year]

    fig = px.scatter(
        filtered_df,
        x='gdpPercap',
        y='lifeExp',
        size='pop',
        color='continent',
        hover_name='country',
        log_x=True,
        size_max=55,
    )

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run(debug=True, port=8054)
