import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

np.random.seed(56)

x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

nx_trace = go.Scatter(x=x_values,
                      y=y_values + 5,
                      mode='markers',
                      name='markers')
nx_data = [nx_trace]
nx_layout = go.Layout(title='Hello Line Chart',
                      xaxis=dict(title='Hello X Axis'),
                      yaxis=dict(title='Hello Y Axis'))
nx_figure = go.Figure(data=nx_data, layout=nx_layout)
pyo.plot(nx_figure, filename='line_chart.html')
