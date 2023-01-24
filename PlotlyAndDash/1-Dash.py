import dash
from dash import dcc
from dash import html

app = dash.Dash()
nx_colors = {'background': '#1ECBE1', 'text': 'white'}
app.layout = html.Div(children=[
    html.H1('Hello Dash', style={
        'textAlign': 'center',
        'color': nx_colors['text']
    }),
    dcc.Graph(id='my-graph', figure={'data': [{
        'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'San Francisco'
    }, {
        'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'New York City'
    }], 'layout': {
        'plot_bgcolor': nx_colors['background'],
        'paper_bgcolor': nx_colors['background'],
        'font': {
            'color': nx_colors['text']
        },
        'title': 'San Francisco vs New York City'
    }})
], style={
    'backgroundColor': nx_colors['background']
})

if __name__ == '__main__':
    app.run_server(debug=True)
