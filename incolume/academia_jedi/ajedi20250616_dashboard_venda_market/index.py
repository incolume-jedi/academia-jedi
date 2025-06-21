# import from folders/theme changer
import dash
import dash_bootstrap_components as dbc

FONT_AWESOME = ['https://use.fontawesome.com/releases/v5.10.2/css/all.css']
app = dash.Dash(__name__, external_stylesheets=FONT_AWESOME)
app.scripts.config.serve_locally = True
server = app.server


# =========  Layout  =========== #
app.layout = dbc.Container(children=[], fluid=True, style={'height': '100vh'})


# ======== Callbacks ========== #

# Run server
if __name__ == '__main__':
    app.run_server(debug=True)
