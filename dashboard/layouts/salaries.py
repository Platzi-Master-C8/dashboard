from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import betterSalariesForModality, betterSalariesForSeniority, allSkills, datasets


def _build_layout():
    _layoutStructure = ["salaries_by_modality .",
                        "skills      salaries_by_seniority"]
    with engine.connect() as conn:
        return layout.grid([
            layout.area(infographic.bars("Salary by modality",
                                         *datasets(["modality", "salary"], betterSalariesForModality(conn))),
                        "salaries_by_modality"),
            layout.area(infographic.bars("Salary by seniority",
                                         *datasets(["seniority", "salary"], betterSalariesForSeniority(conn))),
                        "salaries_by_seniority"),
            layout.area(infographic.wordcloud(*datasets(["skill"], allSkills(conn)),
                                              shape="fa-robot",
                                              size=320,
                                              output_name="assets/all_skills_cloud.png"),
                        "skills")
        ], 2, 2, _layoutStructure)


page = layout.titleAndContent("Salaries", _build_layout())
