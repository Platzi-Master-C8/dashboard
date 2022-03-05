from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import (
    numberOfCompanies,
    numberOfPositions,
    numberOfReviews
)


def _build_layout():
    _layoutStructure = ["companies . reviews",
                        ".  positions   .",
                        "note     note      note"]
    with engine.connect() as conn:
        companies = numberOfCompanies(conn)
        positions = numberOfPositions(conn)
        reviews = numberOfReviews(conn)
        return layout.twoColumns(
            layout.titleAndImage(
                "",
                "assets/sample.gif"
            ),
            layout.grid([
                layout.area(infographic.value("Companies", companies), "companies"),
                layout.area(infographic.value("Positions", positions), "positions"),
                layout.area(infographic.value("Reviews", reviews), "reviews"),
                layout.area(infographic.text("""
                ### Data extracted from:
                
                1. WeWorkRemotley 
                1. GetOnBoard
                1. Indeed
                1. RemoteOK
                """), "note", row_align="start")
            ], 3, 3, _layoutStructure)
        )


page = layout.titleAndContent("Data used", _build_layout())
