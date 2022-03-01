from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import bestPayedSkills, datasets


def _build_layout():
    _layoutStructure = ["salary_popularity ."]
    
    with engine.connect() as conn:
        return layout.grid([
            layout.area(infographic.scatter("Relation popularity salary by skill",
                                         *datasets(["salary", "offers","skill"], 
                                                   bestPayedSkills(conn)
                                                   )
                                         ),
                        "salary_popularity")
        ], 1, 1, _layoutStructure)


page = layout.titleAndContent("salary_popularity", _build_layout())
