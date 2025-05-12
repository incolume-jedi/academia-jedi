"""Example of using states in Dash."""

from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
])


@app.callback(
    Output('output-state', 'children'),
    Input('submit-button-state', 'n_clicks'),
    State('input-1-state', 'value'),
    State('input-2-state', 'value'),
)
def update_output(n_clicks: int, input1: str, input2: str) -> str:
    """Update the output based on the button click and inputs."""
    return f"""
        The Button has been pressed {n_clicks:03} times,
        Input 1 is "{input1.strip()}",
        and Input 2 is "{input2.strip()}"
    """


if __name__ == '__main__':
    app.run(debug=True)
