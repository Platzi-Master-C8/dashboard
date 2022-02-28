from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import betterSalariesForModality, betterSalariesForSeniority, betterOffers, datasets, table


def _build_layout():
    _layoutStructure = ["jobs_table"]
    with engine.connect() as conn:
        return layout.grid([
            layout.area(infographic.table(*table({"modality": "Modality",
                                                  "name": "Company",
                                                  "seniority": "Seniority Level",
                                                  "position_title": "Job",
                                                  "salary": "Salary"}, betterOffers(conn))),
                        "jobs_table")
        ], 1, 1, _layoutStructure)


page = layout.titleAndContent("Jobs", _build_layout())
