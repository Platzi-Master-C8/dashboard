from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import numberOfCompanies, numberOfPositions, numberOfSkills


def _build_layout():
    _layoutStructure = ["companies .        skills",
                        ".      positions   .",
                        ".         .    ."]
    with engine.connect() as conn:
        companies = numberOfCompanies(conn)
        positions = numberOfPositions(conn)
        skills = numberOfSkills(conn)
        return layout.twoColumns(
            layout.titleAndImage(
                "",
                "assets/sample.png"
            ),
            layout.grid([
                layout.area(infographic.value("Companies", companies), "companies"),
                layout.area(infographic.value("Positions", positions), "positions"),
                layout.area(infographic.value("Skills", skills), "skills")
            ], 3, 3, _layoutStructure)
        )


page = layout.titleAndContent("Data used", _build_layout())
