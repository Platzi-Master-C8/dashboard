# Style cloud
import stylecloud

# Plotly
import plotly.express as px
from plotly.subplots import make_subplots
from plotly import graph_objects as go, colors as c

# Dash
from dash import html, dcc, dash_table

# Pandas
from pandas import DataFrame

# Typing
from typing import List

# Styles
from dashboard.styles import layout, infographic, base, colors


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


def bars(title: str, labels: list, values: list):
    fig = go.Figure()
    fig.add_bar(x=labels, y=values, marker_color=c.qualitative.Plotly)
    fig.update_traces(texttemplate='%{y:.2s}', textposition="auto")
    fig.update_layout(title=title, template="plotly_dark", xaxis_tickangle=-45)
    return dcc.Graph(figure=fig, style=base.allArea)


def scatter(title: str, labels: list, values: list):
    fig = go.Figure()
    fig.add_scatter(x=labels, y=values, marker=dict(
        color=c.qualitative.Plotly,
    ))
    fig.update_layout(title=title, template="plotly_dark", xaxis_tickangle=-45)
    return dcc.Graph(figure=fig, style=base.allArea)


def bubbles(title: str, labels: list, values: list, sizes: int):
    fig = go.Figure()
    fig.add_scatter(x=labels, y=values, marker=dict(
        color=c.qualitative.Plotly,
        size=sizes
    ))
    fig.update_layout(title=title, template="plotly_dark", xaxis_tickangle=-45)
    return dcc.Graph(figure=fig, style=base.allArea)


def reputation_bar(df: DataFrame):
    fig = px.bar(
        df,
        x='name',
        y='avg_reputation',
        range_y=[0, 5],
        title='Average Reputation',
        color='name',
        text_auto=True,
    )
    fig.update_layout(
        title_text="Average Reputation",
        template="plotly_dark",
        width=700, )
    return dcc.Graph(figure=fig, style=base.allArea)


def reputation_plot(df: DataFrame):
    fig = make_subplots(
        rows=1,
        cols=1,
        specs=[[{"secondary_y": True}]],
    )
    fig.add_trace(
        go.Bar(
            x=df["name"],
            y=df["culture_score"],
            name="Culture Score",
            width=0.15,
        ),
        row=1, col=1,
        secondary_y=False,
    )
    fig.add_trace(
        go.Bar(
            x=df["name"],
            y=df["perks_score"],
            name="Perks Score",
            width=0.15,
        ),
        row=1, col=1,
        secondary_y=False,
    )
    fig.add_trace(
        go.Bar(
            x=df["name"],
            y=df["work_life_balance_score"],
            name="Work Life Balance Score",
            width=0.15,
        ),
        row=1, col=1,
        secondary_y=False,
    )
    fig.add_trace(
        go.Bar(
            x=df["name"],
            y=df["career_opportunities_score"],
            name="Career Opportunities Score",
            width=0.15,
        ),
        row=1, col=1,
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=df["name"],
            y=df["median"],
            name="Salary Median"
        ),
        row=1, col=1,
        secondary_y=True,
    )

    fig.update_layout(
        title_text="Salary vs Reputation",
        width=600,
        template="plotly_dark",
    )

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Salary</b>", secondary_y=True)
    fig.update_yaxes(title_text="<b>Reputation</b>", secondary_y=False)
    return dcc.Graph(figure=fig, style=base.allArea)


def pie_chart(title: str, labels: list, values: list):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_traces(textinfo='label+percent', textfont_size=20, )
    fig.update_layout(
        title_text=title,
        template="plotly_dark")
    return dcc.Graph(figure=fig, style=base.allArea)
