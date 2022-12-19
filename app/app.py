import os
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

from navbar import navbar
from utils import themes_csv

external_stylesheets = [
    dbc.themes.MORPH
]

themes_df = pd.read_csv(themes_csv)
themes_df = themes_df[['n', 'consolidated_round1_cc',
                       'consolidated_final_cc', 'themes_cc']]
fig_sunburst_raw = px.sunburst(themes_df,
                               path=['themes_cc',
                                     'consolidated_final_cc',
                                     'consolidated_round1_cc'],
                               values='n')
fig_sunburst_raw = fig_sunburst_raw.update_traces(textinfo='label')

layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    width=650,
    height=650,
    title=dict(text='Trail Activities by Themes',
               x=0.5),
    titlefont=dict(size=24, color="#000000"),
    margin=dict(l=50, r=50, b=50, t=50),
    # annotations=[
    #     go.layout.Annotation(
    #         # text='<i>Data source: Climate Watch, the World Resources Institute (2020)</i>',
    #         xanchor='right',
    #         yanchor='top',
    #         showarrow=False,
    #         x=1,
    #         xshift=50,
    #         y=0,
    #         font=dict(size=16, color="#000000", family="Arial")
    #     )
    # ]
)

fig_sunburst = go.Figure(
    go.Sunburst(
        ids=fig_sunburst_raw['data'][0]['ids'].tolist(),
        labels=fig_sunburst_raw['data'][0]['labels'].tolist(),
        parents=fig_sunburst_raw['data'][0]['parents'].tolist(),
        values=fig_sunburst_raw['data'][0]['values'].tolist(),
        # rotation=187,
        branchvalues="total",
        marker=dict(colorscale="Teal",
                    #showscale=True
                    ),
        insidetextorientation='horizontal',
    ),
    layout=layout
)

fig_sunburst = fig_sunburst.update_traces(textinfo='label+percent entry',
                                          insidetextfont=dict(size=20))

app = Dash(__name__,
           external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dbc.Row(navbar()),
    dbc.Row(
        children=[html.Div(dcc.Graph(figure=fig_sunburst),
                           className='pretty_container',
                           style={'width': '50%'})],
        class_name='px-4 navbar-light',
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
