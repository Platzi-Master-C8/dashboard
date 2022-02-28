def _grid_size(sizes):
    if isinstance(sizes, int):
        if sizes == 1:
            return "1fr"
        return f"repeat({sizes}, 1fr)"
    if isinstance(sizes, str):
        return sizes
    return ' '.join(sizes)


def _grid_areas(areas):
    if isinstance(areas, str):
        return areas
    return " ".join([f'"{area}"' for area in areas])


def columns(cols):
    return grid(cols, "1fr")


def grid(cols, rows, col_align="center", row_align="center", areas=None):
    grid_areas = {}
    grid_columns = {}
    grid_rows = {}
    if areas is not None:
        grid_areas = {"gridTemplateAreas": _grid_areas(areas)}
    if columns is not None:
        grid_columns = {"gridTemplateColumns": _grid_size(cols)}
    if grid_rows is not None:
        grid_rows = {"gridTemplateRows": _grid_size(rows)}

    return {"display": "grid",
            "justifyItems": row_align,
            "alignItems": col_align,
            "height": "100%",
            "width": "100%"
            } | grid_columns | grid_rows | grid_areas


titleAndImage = grid("1fr", ["max-content", "1fr"]) | {"gridRowGap": "20px"}

titleAndContent = grid("1fr", ["max-content", "1fr"]) | {"gridRowGap": "20px"}

infographicValue = grid("1fr", ["1fr", "max-content"])
