from urllib.parse import unquote
from dash import html, dcc, Dash
from dashboard.layouts import start, sample_size, salaries, salaries_table
from dashboard.styles import base
from dashboard.components.navigation import route
from jupyter_dash import JupyterDash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

navigation = {
    "start": (None, "sample_size", start.page),
    "sample_size": ("start", "salaries", sample_size.page),
    "salaries": ("sample_size", "salaries_table", salaries.page),
    "salaries_table": ("salaries", None, salaries_table.page)
}

routes = {key: route(previous, next, layout) for key, (previous, next, layout) in navigation.items()}


def run_app(embedded=True):
    dash_builder = JupyterDash if embedded else Dash
    app = dash_builder("Job Placement", external_stylesheets=[
        dbc.themes.BOOTSTRAP, dbc.themes.DARKLY])
    del app.config._read_only["requests_pathname_prefix"]

    main_workspace = html.Div([
        dcc.Location(id="location"),
        html.Div(id="main_content", style=base.allArea)
    ], style=base.workspace)

    layouts = [main_workspace]
    for layout in routes.values():
        layouts.append(layout)

    app.validation_layout = html.Div(layouts)
    app.layout = main_workspace

    @app.callback(Output("main_content", "children"),
                  Input("location", "pathname"))
    def display_layout(pathname):
        print(unquote(pathname)[1:])
        return routes.get(unquote(pathname)[1:], routes["start"])

    if embedded:
        app.run_server(mode="inline", height=600, width="100%")
    else:
        app.run_server(debug=True)
