import os
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

from dash import Dash, html, dcc, Input, Output, ctx
import dash_bootstrap_components as dbc

from charts import covid_barchart, activity_choropleth, demographic_chord
from navbar import navbar
from utils import *

external_stylesheets = [
    dbc.themes.MORPH,
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
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

sunburst_layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, b=0, t=10)
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
    layout=sunburst_layout
)

fig_sunburst = fig_sunburst.update_traces(textinfo='label+percent entry',
                                          insidetextfont=dict(size=20))

covid_questions_dict = dict(zip(covid_questions_full, covid_questions))

app = Dash(__name__,
           external_stylesheets=external_stylesheets)
app.title = 'Trails Dashboard'

slider_marks = {5*i: f'{5*i}' for i in range(5)}
slider_marks[1] = '1'

app.layout = html.Div([
    dbc.Row(navbar()),
    dbc.Row([html.Div([html.H3('Introduction', className='intro_text'),
                       html.P(html_text_intro,
                              style={'margin': '0px 10px',
                                     'padding': '0px 25px'})],
                      style={'width': '21%'}),
             html.Div(html.Img(src="assets/images/IMG_7093.jpeg",
                               style={'width': '100%',
                                      'height': 'auto',
                                      'padding': '25px',
                                      'margin': '70px 10px 10px',
                                      'border-radius': '10%'}),
                      style={'width': '23%'}),
             html.Div([html.H5('Geographic Distribution of Activities '
                               'on Trails'),
                       dcc.Dropdown(id="activity_choropleth_dropdown",
                                    options=top_20_activities,
                                    value='Hike',
                                    clearable=False,
                                    className='dropdown'),
                       dcc.Graph(id='activity_choropleth',
                                 # responsive=True,
                                 config={'displayModeBar': 'hover'})],
                      className='pretty_container',
                      style={'width': '54%'})],
            className='px-4'),
    dbc.Row(
        children=[html.Div([html.H5('To what extent has COVID-19 changed '
                                    'your experience of trails compared '
                                    'to during pre-COVID times?'),
                            dcc.Dropdown(id="covid_barchart_dropdown",
                                         options=covid_questions_full,
                                         value='Number people on trails',
                                         clearable=False,
                                         className='dropdown'),
                            dcc.Graph(id='covid_barchart',
                                      responsive=True,
                                      style={'height': '430px'}),
                            html.P(html_text_covid,
                                   style={'font-size': '0.8em'})],
                           className='pretty_container',
                           style={'width': '54%'}),
                  html.Div([html.H5('Activities on Trails'),
                            dcc.Graph(figure=fig_sunburst,
                                      responsive=True,
                                      style={'height': '450px'}),
                            html.P(html_text_sunburst,
                                   style={'font-size': '0.8em',
                                          'margin-top': '10px'})],
                           className='pretty_container',
                           style={'width': '43%'})
                  ],
        class_name='px-4'
    ),
    dbc.Row(
        children=[html.Div([html.H5('Activities and Demographics'),
                            html.Button('Age', id='btn-age', n_clicks=0,
                                        n_clicks_timestamp=0,
                                        className='chord_button age_btn'),
                            html.Button('Education', id='btn-edu', n_clicks=0,
                                        n_clicks_timestamp=0,
                                        className='chord_button edu_btn',
                                        autoFocus=True),
                            dbc.Row([
                                html.Div(
                                    [dcc.Slider(1, 20, 1,
                                                value=5,
                                                id='chord-slider',
                                                marks=slider_marks,
                                                vertical=True,
                                                verticalHeight='465'),
                                     html.P('Top',
                                            style={'font-size': '10pt',
                                                   'margin-top': '-15px'})],
                                    style={'width': '7%'}
                                ),
                                html.Div(
                                    html.Iframe(id="chord-diagram",
                                                srcDoc=None,
                                                style={'height': '100%',
                                                       'width': '100%'}),
                                    style={'width': '90%'}
                                )]),
                            html.P(html_text_chord,
                                   style={'font-size': '0.8em'})
                            ],
                           className='pretty_container',
                           style={'width': '43%'}),
                  html.Div([html.Img(src="assets/images/IMG_0521.jpeg",
                                     style={'width': '100%',
                                            'height': 'auto',
                                            'padding': '25px',
                                            'margin': '10px 10px',
                                            'border-radius': '8%'})],
                           style={'width': '54%'})
                  ],
        class_name='px-4'
    )
])


@app.callback(
    Output("activity_choropleth", "figure"),
    Input("activity_choropleth_dropdown", "value"))
def update_activity_choropleth(actv):
    return activity_choropleth(actv)


@app.callback(
    Output("covid_barchart", "figure"),
    Input("covid_barchart_dropdown", "value"))
def update_covid_barchart(q):
    return covid_barchart(covid_questions_dict[q])


@app.callback(
    Output('chord-diagram', 'srcDoc'),
    Input('btn-age', 'n_clicks_timestamp'),
    Input('btn-edu', 'n_clicks_timestamp'),
    Input('chord-slider', 'value')
)
def update_chord_chart(btn_age, btn_edu, top_n):
    if 'btn-age' == ctx.triggered_id:
        return demographic_chord(top_n, 'AGE')
    elif 'btn-edu' == ctx.triggered_id:
        return demographic_chord(top_n, 'EDUCATION')
    else:
        if btn_age > btn_edu:
            return demographic_chord(top_n, 'AGE')
        else:
            return demographic_chord(top_n, 'EDUCATION')


if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0",
                   port=int(os.environ.get('PORT', 8080)))
