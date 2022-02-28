from dash.development.base_component import Component


def size(width, height):
    return {"width": width, "height": height}


workspace = size("100vw", "100vh") | {
    "padding": "20px"
}

allArea = size("100%", "100%")

center = {
    "textAlign": "center"
}

width100 = {
    "width": "100%"
}


def append(element: Component, styles: dict):
    try:
        element.style = element.style | styles
    except:
        element.style = styles
    return element
