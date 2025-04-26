"""Estudos com dash."""
import dash
import plotly.express as px
import pandas as pd

stylesheets = [
'https://pastebin.com/raw/rbW8zaDe',
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)


df0 = pd.DataFrame({
    'Fruit':['Apple', 'Orange', 'Banana', 'Grapes', 'Apple', 'Banana'],
    'Amount':[4, 1, 2,2,4, 5],
    'City':['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal'],},
)

fig = px.bar(df0, x='Fruit', y='Amount', color='City')


app.layout = dash.html.Div(
    id='div1',
    children=[
        dash.html.H1(children='Hello Dash'),
        dash.html.Div(children='''Dash: A web application framework for Python.'''),
        dash.dcc.Graph(
            id='graph',
            figure=fig
    )
])

if __name__ == "__main__":
    # Executa o script principal
    app.run(debug=True, port=8050)
