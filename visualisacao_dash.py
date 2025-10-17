import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output 
import plotly.express as px

df = pd.read_csv('ecommerce_estatistica.csv')
df.head()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('E-commerce Data Dashboard'),

    html.Div([
        dcc.Dropdown(
            id='feature-dropdown',
            options=[{'label': col, 'value': col} for col in df.columns],
            value=df.columns[0]
        ),
    ]),

    html.Div([
        dcc.Graph(id='feature-graph')
    ])
])



@app.callback(
    Output('feature-graph', 'figure'),
    Input('feature-dropdown', 'value')
)
def update_graph(selected_feature):
    fig = px.histogram(df, x=selected_feature)
    return fig

if __name__ == '__main__':
    app.run(debug=False)