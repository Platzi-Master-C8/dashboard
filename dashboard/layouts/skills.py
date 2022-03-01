from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import mostRequestedSkills, bestPayedSkills, datasets


def _build_layout():
    _layoutStructure = ["most_requested_skills .",
                        ".      salaries_by_seniority"]
    with engine.connect() as conn:
        return layout.grid([
            layout.area(infographic.bars("Most Requested Skills",
                                         *datasets(["skill", "count"], mostRequestedSkills(conn))),
                        "most_requested_skills"),
            layout.area(infographic.bars("Best payed skills",
                                         *datasets(["skill", "salary"], bestPayedSkills(conn))),
                        "best_payed_skills")
        ], 2, 2, _layoutStructure)


page = layout.titleAndContent("skills", _build_layout())
