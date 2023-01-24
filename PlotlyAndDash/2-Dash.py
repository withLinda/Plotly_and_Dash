import dash
from dash import html, dcc
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div([
    dcc.Graph(id='scatter-graph', figure={
        'data': [go.Scatter(
            x=random_x,
            y=random_y,
            mode='markers')],
        'layout': go.Layout(
            title='Scatter Plot')
    })
])

if __name__ == '__main__':
    app.run_server(debug=True)
