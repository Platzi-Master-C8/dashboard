from dash import html
from dashboard.styles import base, layout


def titleAndImage(title: str, img_src: str):
    return html.Div([html.Div(
        children=[
            html.H1(title,
                    style=base.center | base.width100),
            html.Img(src=img_src, style={"width": "100%",
                                         "backgroundSize": "cover"})
        ],
        style=base.allArea | layout.titleAndImage
    )])


def titleAndContent(title: str, content):
    return html.Div(
        children=[
            html.H1(title,
                    style=base.center | base.width100),
            content
        ],
        style=base.allArea | layout.titleAndContent
    )


def twoColumns(left, right, left_size="1fr", right_size="1fr"):
    return html.Div([
        left,
        right
    ], style=layout.columns([left_size, right_size]))


def grid(children, columns=1, rows=1, areas=None):
    return html.Div(children, style=layout.grid(columns, rows, areas=areas))


def area(element, area: str, col_align="center", row_align="center"):
    if area is None:
        return element
    base.append(element, {"gridArea": area,
                          "alignSelf": col_align,
                          "justifySelf": row_align})
    return element


def empty():
    return html.Div(style={})
