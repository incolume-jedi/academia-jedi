"""Dash callback in chain example."""

from dash import Dash, Input, Output, dcc, html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': ['Montréal', 'Toronto', 'Ottawa'],
    'Brazil': ['Brasília', 'São Paulo', 'Manaus', 'Pernambuco'],
}
app.layout = html.Div([
    dcc.RadioItems(
        list(all_options.keys()),
        'Brazil',
        id='countries-radio',
    ),
    html.Hr(),
    dcc.RadioItems(id='cities-radio'),
    html.Hr(),
    html.Div(id='display-selected-values'),
])


@app.callback(
    Output('cities-radio', 'options'),
    Input('countries-radio', 'value'),
)
def set_cities_options(selected_country: str) -> list[dict[str, str]]:
    """Set the options for the cities based on the selected country."""
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    Output('cities-radio', 'value'),
    Input('cities-radio', 'options'),
)
def set_cities_value(available_options):
    """Set the default value for the cities radio button.

    Parameters
    ----------
    available_options : list of dict
        List of available city options with 'label' and 'value' keys.

    Returns:
    -------
    str
        The value of the first available city option.
    """
    return available_options[0]['value']


@app.callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value'),
)
def set_display_children(selected_country: str, selected_city: str) -> str:
    """Display the selected city and country.

    Parameters
    ----------
    selected_country : str
        The selected country.
    selected_city : str
        The selected city.

    Returns:
    -------
    str
        A string describing the selected city and country.
    """
    return f'{selected_city} is a city in {selected_country}'


if __name__ == '__main__':
    app.run(debug=True)
