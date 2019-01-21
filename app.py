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
import plotly.graph_objs as go

df = pd.read_csv("https://raw.githubusercontent.com/rutgerhofste/dash_app_example/master/wef_global_risk_v02.csv")

print(df.shape)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    html.Label('Slider'),

    dcc.Slider(
        min=2012,
        max=2019,
        marks = {1:"2012",2:"2013",3:"2014",4:"2015",5:"2016",6:"2017",7:"2018",8:"2019"},
        value=2019,
    ),

    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['year'] == i]['x'],
                    y=df[df['year'] == i]['y'],
                    text=df[df['year'] == i]['risk'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=str(i)
                ) for i in df.year.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'likelihood'},
                yaxis={'title': 'impact'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])




if __name__ == '__main__':
    app.run_server(debug=True)