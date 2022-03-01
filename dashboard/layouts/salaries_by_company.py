from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import companiesWithBetterSalaries, companiesWithLowestSalaries, datasets


def _build_layout():
    _layoutStructure = ["companies_with_highest_salaries",
                        "companies_with_lowest_salaries"]
    with engine.connect() as conn:
        return layout.twoColumns(
            layout.titleAndImage("", "assets/salary.gif"),
            layout.grid([
                layout.area(infographic.bars("Highest salaries",
                                             *datasets(["name", "salary"], companiesWithBetterSalaries(conn))),
                            "companies_with_highest_salaries"),
                layout.area(infographic.bars("Lowest salaries",
                                             *datasets(["name", "salary"], companiesWithLowestSalaries(conn))),
                            "companies_with_lowest_salaries")
            ], 1, 2, _layoutStructure))


page = layout.titleAndContent("Salaries by companies", _build_layout())
