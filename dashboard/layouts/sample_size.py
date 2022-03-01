from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import (
    numberOfCompanies,
    numberOfPositions,
    numberOfSkills,
    numberOfReviews
)


def _build_layout():
    _layoutStructure = ["companies .        skills",
                        ".      positions   .",
                        "note     note      note"]
    with engine.connect() as conn:
        companies = numberOfCompanies(conn)
        positions = numberOfPositions(conn)
        skills = numberOfSkills(conn)
        reviews = numberOfReviews(conn)
        return layout.twoColumns(
            layout.titleAndImage(
                "",
                "assets/sample.png"
            ),
            layout.grid([
                layout.area(infographic.value("Companies", companies), "companies"),
                layout.area(infographic.value("Positions", positions), "positions"),
                layout.area(infographic.value("Skills", skills), "skills"),
                layout.area(infographic.text("""
                ### Data extracted from:
                
                1. weworkremotley
                1. getonboard
                1. indeed
                """), "note", row_align="start")
            ], 3, 3, _layoutStructure)
        )


page = layout.titleAndContent("Data used", _build_layout())
