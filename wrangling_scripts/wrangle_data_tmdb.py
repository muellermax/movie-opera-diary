import pandas as pd
import numpy as np
import plotly.graph_objs as go

df_movie_tmdb = pd.read_csv('https://raw.githubusercontent.com/muellermax/movie-opera-diary/master/wrangling_scripts/input_tmdb.csv')

def return_figures_tmdb():
    """
    Creates the plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # Plots distplot of difference between my evaluation and tmdb    
    df = df_movie_tmdb.copy()

    # Select only the diff-column
    input_var = df['diff']

    graph_one = [go.Histogram(
        x = input_var)]

    layout_one = dict(title='Distribution of the difference between TMDBs and my own evaluation',
                    xaxis=dict(title='Count'),
                    yaxis=dict(title='Difference (absolute)')
                    )

    #print(input_var)

    # append all charts to the figures list
    figures_tmdb = []
    figures_tmdb.append(dict(data=graph_one, layout=layout_one))

    return figures_tmdb




