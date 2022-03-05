import pandas as pd

from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import remotePositions


def _build_layout():
    _layoutStructure = ['remote_positions']

    with engine.connect() as conn:
        df = pd.read_sql(remotePositions(), conn)
        return layout.grid([
            layout.area(infographic.pie_chart('Remote Works', ['No Remote', 'Remote'], df['count']),
                        'remote_positions'),
        ], 1, 1, _layoutStructure)


page = layout.titleAndContent('Remote Works', _build_layout())
