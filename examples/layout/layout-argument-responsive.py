import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import pandas as pd

import dash_draggable


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app.layout = html.Div([
    html.H1("Dash Draggable"),
    html.B("Description:"),
    html.Ul([
        html.Li("The chart is not draggable nor resizeable (with the value 'static' set to True in 'layout')."),
        html.Li("The slider is draggable and resizeable.")
    ]),
    dash_draggable.ResponsiveGridLayout(
        id='draggable',
        clearSavedLayout=True,
        layouts={
            "lg": [{
                "i": "graph-with-slider",
                "x":0, "y":0, "w":6, "h":12, "static": True
            },
            {
                "i": "year-slider",
                "x": 0, "y":13, "w":6, "h":2
            }],
            "sm": [{
                "i": "graph-with-slider",
                "x":0, "y":0, "w":6, "h":12, "static": True
            },
            {
                "i": "year-slider",
                "x": 0, "y":13, "w":6, "h":2
            },]
        },
        children=[
            dcc.Graph(
                id='graph-with-slider',
                responsive=True,
                style={
                    "width":"100%",
                    "height":"100%",

                }),
            dcc.Slider(
                id='year-slider',
                min=df['year'].min(),
                max=df['year'].max(),
                value=df['year'].min(),
                marks={str(year): str(year) for year in df['year'].unique()},
                step=None)
        ]
    ),
])





@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')
