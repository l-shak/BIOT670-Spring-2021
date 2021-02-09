# import statements to ensure all required packages are imported
# Some of the imports will be needed for later features such as allowing the user to select files
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import base64
import io

import pandas as pd
file_options = []

app = dash.Dash(__name__)
app.title = 'Quad-Viewer'

app.layout = html.Div([
    html.H1(children='Welcome to the Quad-Viewer Application', id='Header', style={
        'textAlign': 'center',
            'fontFamily': 'sans-serif'
    }
            ),
    html.H3(children='Select file(s) you wish to upload:', id='upload_instructions', style={
        'textAlign': 'center',
            'fontFamily': 'sans-serif'
    }
            ),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            html.Button('Upload File(s)')
        ]),
        style={
            'textAlign': 'center'
        },

        # Allow multiple files to be uploaded
        multiple=True
    ),

    dcc.Dropdown(id = 'file-dropdown',
                 style = {'width':'50%', 'align-items': 'center', 'justify-content': 'center'},
                 options= file_options),

])


@app.callback(Output('file-dropdown', 'options'),
              Input('upload-data', 'filename'))
def drop_down(list_of_names):
    if list_of_names is not None:
        for i in list_of_names:
            option = {'label': i, 'value': i}
            file_options.append(option)
        return file_options
    else:
        return ([{'label': '', 'value': ''}])


if __name__ == '__main__':
    app.run_server(debug=True)
