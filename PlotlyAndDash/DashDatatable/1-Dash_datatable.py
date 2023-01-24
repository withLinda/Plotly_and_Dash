import dash
from dash import html, dcc
import dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# import CSV file into pandas dataframe
df = pd.read_csv('internet_cleaned.csv')
df = df[df['year'] == 2019]

# creating an ID column name
df['id'] = df['iso_alpha3']
df.set_index('id', inplace=True, drop=False)
print(df.columns)

# app layout
# app = dash.Dash(__name__, prevent_initial_callbacks=True)
# app.layout = html.Div([
#     dash_table.DataTable(
#         id="datatable-interactivity",
#         columns=[
#             {"name": i, "id": i, "deletable"=True, "selectable": True, "hideable": True}
#             if i == "iso_alpha3" or i == "year" or i == "id"
#             else {"name": i, "id": i, "deletable": True, "selectable": True}
#             for i in df.columns
#         ],
#     data = df.to_dict('records'),
#     editable=True,
#     filter_action="native",
#     sort_action="native",
#     sort_mode="single",
#     column_selectable="multi",
#     row_selectable="multi",
#     row_deletable=True,
#
#
# )
# ])

