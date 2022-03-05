# Pandas
import pandas as pd
# Dashboard
from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import companiesReputation


def _build_layout():
    _layoutStructure = ['companies_reputation']
    with engine.connect() as conn:
        df_reputations = pd.read_sql(companiesReputation(), conn)
        return layout.grid([
            layout.area(infographic.reputation_plot(df_reputations), 'companies_reputation'),
        ], 1, 1, _layoutStructure)


page = layout.titleAndContent('Companies Reputation', _build_layout())
