from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import mostRequestedSkills, lessRequestedSkills, datasets


def _build_layout():
    _layoutStructure = ['most_requested_skills less_requested_skills']
    with engine.connect() as conn:
        return layout.grid([
            layout.area(infographic.bars('Most Requested Skills',
                                         *datasets(['skill', 'count'], mostRequestedSkills(conn))),
                        'most_requested_skills'),
            layout.area(infographic.bars('Less Requested Skills',
                                         *datasets(['skill', 'count'], lessRequestedSkills(conn))),
                        'less_requested_skills')
        ], 2, 1, _layoutStructure)


page = layout.titleAndContent('Popular Skills in Tech', _build_layout())
