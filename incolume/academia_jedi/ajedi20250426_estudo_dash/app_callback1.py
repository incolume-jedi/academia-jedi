"""Model dash."""

import dash
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State

__all__ = ['px', 'pd', 'State']

app = dash.Dash(__name__)


app.layout = dash.html.Div(
    [
    dash.html.H1(children='Estudo com callback'),
    dash.html.Div([
        dash.html.Label('Altere o valor abaixo para ver o callback em ação!'),
        dash.html.Br(),
        dash.html.Br(),
        'Entrada:',
        dash.dcc.Input(id='input1', value='Valor inicial', type='text'),
        dash.html.Br(),
        dash.html.Div(id='output1' ),
    ]
    )
    ]
)

@app.callback(
    Output(component_id='output1', component_property='children'),
    [Input(component_id='input1', component_property='value')],
)
def update_output_div(value):
    """update_output_div.

    Args:
        value (_type_): _description_
    """
    return 'Saída: {}'.format(value)


if __name__ == '__main__':
    app.run(debug=True, port=8053)
