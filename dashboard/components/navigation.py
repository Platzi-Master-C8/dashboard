from dash import dcc
from dashboard.styles import base
from dashboard.components import layout

_layoutStructure = ['content content',
                    'previous next']


def route(previous, next, content):
    return base.append(
        layout.grid([
            base.append(content, {'gridColumn': 'span 2'}),
            base.append(
                dcc.Link(['Previous'],
                         href=previous,
                         className='btn btn-secondary') if previous is not None else layout.empty(),
                {'justify-self': 'end'}),
            base.append(
                dcc.Link(['Next'],
                         href=next,
                         className='btn btn-primary') if next is not None else layout.empty(),
                {'justify-self': 'start'})
        ], ['1fr', '1fr'], ['1fr', 'max-content'], _layoutStructure),
        {'gridColumnGap': '10px',
         'gridRowGap': '20px'})
