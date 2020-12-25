import pandas as pd
import numpy as np
import plotly.graph_objs as go

df_movie_tmdb = pd.read_csv('https://raw.githubusercontent.com/muellermax/movie-opera-diary/master/wrangling_scripts/input_tmdb.csv')


def return_figures_tmdb():
    """
    Creates the plotly visualizations

    Input:
        None

    Output:
        list (dict): list containing the four plotly visualizations#
    """

    # Plots distplot of difference between my evaluation and tmdb    
    df = df_movie_tmdb.copy()

    # Sort by difference
    df = df.sort_values('diff', ascending = False)
    df = df['diff']
    group_labels = ['distplot']

    graph_one = go.Figure(go.distplot(df, group_labels))    

    layout_one = dict(title='The 15 most viewed directors/composers',
                    xaxis=dict(title='Number of views'),
                    yaxis=dict(title='Average evaluation')
                    )

    figures_tmdb = []
    figures_tmdb.append(dict(data=graph_one, layout=layout_one))
       # https://plotly.com/python/distplot/


