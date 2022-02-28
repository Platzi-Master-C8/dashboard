from dash import html, dcc, dash_table
from dashboard.styles import layout, infographic, base, colors
from plotly import graph_objects as go, colors as c
from typing import List


def info(data: any):
    children = data if isinstance(data, list) else [data]
    return html.Div(children, className="text-info")


def value(label: str, value: int, color=colors.YELLOW):
    return html.Div([
        html.Span(f"{value:,}", style=infographic.value | {"color": color}),
        html.Span(label, style=infographic.label),
    ], style=layout.infographicValue)


def table(dataset: List[dict], columns: dict, styles: dict = infographic.data_table):
    return dash_table.DataTable(dataset,
                                [{"name": label, "id": id} for id, label in columns.items()],
                                **styles,
                                virtualization=True)


def bars(title, labels, values):
    fig = go.Figure()
    fig.add_bar(x=labels, y=values, marker_color=c.qualitative.Plotly)
    fig.update_traces(texttemplate='%{y:.2s}', textposition="auto")
    fig.update_layout(title=title, template="plotly_dark", xaxis_tickangle=-45)
    return dcc.Graph(figure=fig, style=base.allArea)
