"""Study Dash with global variables."""

import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash(__name__)

df0 = pd.DataFrame({
    'student_id': range(1, 11),
    'score': [1, 5, 2, 5, 2, 3, 1, 5, 1, 5],
})

app.layout = html.Div([
    dcc.Dropdown(list(range(1, 6)), 1, id='score'),
    'Foi pontuado pela seguinte quantidade de estudantes:',
    html.Div(id='output'),
    dcc.Store(id='store'),
])


@app.callback(Output('store', 'data'), Input('score', 'value'))
def update_output(value: int) -> dict:
    """Update output.

    Update the store with the filtered
    DataFrame based on the selected score.
    """
    filtered_df = df0[df0['score'] == value]
    return filtered_df.to_dict()


@app.callback(Output('output', 'children'), Input('store', 'data'))
def update_output(data: dict) -> pd.DataFrame:
    """Update output.

    Update the output with the number of students
    who scored the selected score.
    """
    filtered_df = pd.DataFrame(data)
    return len(filtered_df)


if __name__ == '__main__':
    app.run(debug=True)
