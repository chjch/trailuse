from io import StringIO
import numpy as np
import pandas as pd
import plotly.express as px
import holoviews as hv
from holoviews import opts, dim

from utils import *

hv.extension('bokeh')

response_df = pd.read_csv(response_csv)

covid_df = response_df[covid_questions].iloc[2:]
covid_df = covid_df.reset_index(drop=True)
covid_df = covid_df.dropna()


def covid_barchart(q: str):
    covid_q_df = covid_df[q].value_counts().to_frame() \
                            .reindex(response_order) \
                            .reset_index() \
                            .rename(columns={'index': 'response',
                                             q: 'count'})
    fig = px.bar(covid_q_df, x='response', y='count')
    fig.update_traces(marker_color='rgb(158,202,225)',
                      marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5, opacity=0.6)
    return fig


states_df = response_df[[rid_column, state_column]].iloc[2:].dropna()
states_df[rid_column] = states_df.ResponseId.str.lower()
states_df['STATEABBREV'] = states_df[state_column].apply(
    lambda x: us_state_to_abbrev.get(x)
)

activity_df = pd.read_csv(activity_csv)
activity_df = activity_df[[rid_column, actv_column]]

activity_state_df = activity_df.join(states_df.set_index(rid_column),
                                     on=rid_column).dropna()


def activity_choropleth(actv: str):
    mask = activity_state_df[actv_column] == actv.lower()
    statecounts_df = activity_state_df[mask].groupby('STATEABBREV') \
                                            .agg({rid_column: 'count',
                                                  state_column: 'first'}) \
                                            .reset_index()
    fig = px.choropleth(statecounts_df,
                        locations='STATEABBREV',
                        locationmode="USA-states",
                        color=rid_column,
                        color_continuous_scale="Darkmint",
                        hover_name='Q24',
                        hover_data={'STATEABBREV': False, rid_column: True},
                        labels={rid_column: 'Number'},
                        scope="usa")
    fig.update_layout(dragmode=False, margin=dict(l=0, r=0, b=0, t=30))
    fig.update_geos(showlakes=False)
    return fig


demogr_actv_df = pd.read_csv(demogr_actv_csv)
demogr_actv_df = demogr_actv_df[[rid_column, actv_column,
                                 GENDER, EDUCATION, AGE]]


def demographic_chord(top_n, demogr_type):
    top_actv = demogr_actv_df[actv_column].value_counts()[:top_n].index.values
    top_actv_d = pd.Series(np.arange(top_n), index=top_actv).to_dict()
    mask = demogr_actv_df[actv_column].isin(top_actv)
    # indexing activity
    demogr_actv_df.loc[mask, 'idx_actv'] = (
        demogr_actv_df[mask][actv_column].apply(lambda x: top_actv_d.get(x))
    )
    if demogr_type.lower() == 'age':
        demogr_list = np.sort(demogr_actv_df[mask].AGE.unique()) \
                        .astype(int) \
                        .astype(str)
    elif demogr_type.lower() == 'education':
        demogr_list = sorted(demogr_actv_df.EDUCATION.unique(),
                             key=edu_order.index)
    else:
        raise ValueError("Not a valid option to create a chord diagram.")
    nodes_sr = pd.Series(np.concatenate([top_actv, demogr_list]))
    nodes_df = nodes_sr.reset_index().rename(columns={0: 'name'})

    demogr_list_d = pd.Series(
        np.arange(top_n, len(demogr_list) + top_n),
        index=demogr_list
    ).to_dict()
    # indexing demographic
    demogr_actv_df.loc[mask, 'idx_demogr'] = (
        demogr_actv_df[mask][demogr_type.upper()].astype(str)
        .apply(lambda x: demogr_list_d.get(x))
    )

    links_data = []
    for i in range(top_n):
        for j in np.arange(len(demogr_list)) + top_n:
            n = len(
                demogr_actv_df[mask][(demogr_actv_df[mask]['idx_actv'] == i) &
                                     (demogr_actv_df[mask]['idx_demogr'] == j)]
            )
            if n != 0:
                links_data.append([i, j, n])
    links_df = pd.DataFrame(links_data, columns=['source', 'target', 'value'])

    nodes = hv.Dataset(nodes_df, 'index')
    mycmap = px.colors.qualitative.Vivid
    mycmap.append('rgb(187, 197, 170)')
    mycmap.append('rgb(249, 145, 204)')
    chord = hv.Chord((links_df, nodes))
    chord.opts(
        opts.Chord(cmap=mycmap,
                   edge_cmap=mycmap,
                   toolbar=None,
                   edge_color=dim('source').str(),
                   labels='name',
                   edge_alpha=0.8,
                   edge_line_width=1,
                   node_line_width=1,
                   node_color=dim('index').str(),
                   width=450, height=450),
    )
    html_chord = StringIO()
    hv.save(chord, html_chord)
    return html_chord.getvalue()
