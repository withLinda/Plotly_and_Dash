import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

nx_data = [go.Scatter(x=random_x,
                      y=random_y,
                      mode='markers',
                      marker=dict(
                          size=10,
                          opacity=0.5,
                          color='rgb(51,204,153)',
                          symbol='pentagon',
                          line=dict(width=2,
                                    color='blue',
                                    )))]
nx_layout = go.Layout(title="HELLO Scatter Example",
                      xaxis=dict(title="HELLO X AXIS"),
                      yaxis=dict(title="HELLO Y AXIS"),
                      hovermode='closest')

# this has the same output:
# nx_layout = go.Layout(title="HELLO Scatter Example",
#                       xaxis=go.layout.XAxis(title="HELLO X AXIS"),
#                       yaxis=go.layout.YAxis(title="HELLO Y AXIS"),
#                       hovermode='closest')

nx_figure = go.Figure(data=nx_data, layout=nx_layout)
pyo.plot(nx_figure, filename='scatter.html')
