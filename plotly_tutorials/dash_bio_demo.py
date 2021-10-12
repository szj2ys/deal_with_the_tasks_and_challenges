# *_*coding:utf-8 *_*
from __future__ import absolute_import, division, print_function
import dash
from dash.dependencies import Input, Output
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)

sequences = {
    'PDB_01019': {
        'sequence': 'AUGGGCCCGGGCCCAAUGGGCCCGGGCCCA',
        'structure': '.((((((())))))).((((((()))))))'
    },
    'PDB_00598': {
        'sequence': 'GGAGAUGACgucATCTcc',
        'structure': '((((((((()))))))))'
    }
}

app.layout = html.Div([
    dashbio.FornaContainer(id='my-default-forna'),
    html.Hr(),
    html.P('Select the sequences to display below.'),
    dcc.Dropdown(id='my-default-forna-sequence-display',
                 options=[{
                     'label': name,
                     'value': name
                 } for name in sequences.keys()],
                 multi=True,
                 value=['PDB_01019'])
])


@app.callback(Output('my-default-forna', 'sequences'),
              Input('my-default-forna-sequence-display', 'value'))
def show_selected_sequences(value):
    if value is None:
        raise PreventUpdate
    return [sequences[selected_sequence] for selected_sequence in value]


if __name__ == '__main__':
    app.run_server(debug=True)
