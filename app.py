# -*- coding: utf-8 -*-

# virtual env python 3.7

#pip install dash==0.35.1  # The core dash backend
#pip install dash-html-components==0.13.4  # HTML components
#pip install dash-core-components==0.42.1  # Supercharged components
#pip install dash-table==3.1.11  # Interactive DataTable component (new!)
#conda install pandas

import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv("https://raw.githubusercontent.com/rutgerhofste/dash_app_example/master/wef_global_risk_v02.csv")

print(df.shape)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [10, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("rows"),
    )
])




if __name__ == '__main__':
    app.run_server(debug=True)