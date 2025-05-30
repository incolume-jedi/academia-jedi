"""Model dash."""

import dash
import pandas as pd
import plotly.express as px

__all__ = ['pd', 'px']

app = dash.Dash(__name__)


app.layout = dash.html.Div(dash.html.H1(children='Hello Dash'))

if __name__ == '__main__':
    app.run(debug=True, port=8050)
