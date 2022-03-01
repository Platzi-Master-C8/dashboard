from dash import html, dcc, dash_table
from dashboard.styles import layout, infographic, base, colors
from plotly import graph_objects as go, colors as c
from typing import List
import stylecloud


def wordcloud(words: list, shape: str, size: int, output_name: str):
    words = " ".join(words)
    stylecloud.gen_stylecloud(text=words,
                              icon_name=f'fas {shape}',
                              palette='colorbrewer.diverging.Spectral_11',
                              background_color="black",
                              output_name=output_name,
                              size=size,
                              gradient='horizontal')
    return html.Img(src=output_name, style={"width": f"{size}px",
                                            "height": f"{size}px",
                                            "backgroundSize": "cover"})


def text(text: str):
    return dcc.Markdown(text)


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


def scatter(title, labels, values ,names):
    fig = go.Figure()
    fig.add_scatter(x=labels, y=values, 
                    # marker=dict(
        # color=c.qualitative.Plotly,
    # )
    )
    fig.update_layout(title=title, template="plotly_dark", xaxis_tickangle=-45)
    return dcc.Graph(figure=fig, style=base.allArea)


def bubbles(title, labels, values, sizes):
    fig = go.Figure()
    fig.add_scatter(x=labels, y=values, marker=dict(
        color=c.qualitative.Plotly,
        size=sizes
    ))
    fig.update_layout(title=title, template="plotly_dark", xaxis_tickangle=-45)
    return dcc.Graph(figure=fig, style=base.allArea)
