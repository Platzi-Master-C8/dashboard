from statistics import median
from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import betterSalaryForRemote, datasets


def _build_layout():
    _layoutStructure = ["Salary for remote offers."]
    with engine.connect() as conn:
        return layout.grid([
            layout.area(infographic.bars("Most Requested Skills",
                                         *datasets([ "remote", "median"], betterSalaryForRemote(conn))),
                        "better_salary_for_remote")
        ], 1, 2, _layoutStructure)


page = layout.titleAndContent("better_salary_for_remote", _build_layout())
