import pandas as pd
import numpy as np
import plotly.graph_objs as go

df_movie_tmdb = pd.read_csv('https://raw.githubusercontent.com/muellermax/movie-opera-diary/master/wrangling_scripts/input_tmdb.csv')

def me_vs_tmdb_results(df, m):
    """
    Function to show the difference of the m items with the highest and lowest 
    difference in the evaluation. A positive value means that my evaluation is 
    higher than the tmdb average. 
    
    Input: 
        df (DataFrame): DataFrame with the difference in the evaluations.
        m (int): How many items should be included (e.g. 'Top-30')
        
    Output: 
        A Seaborn plot. 
    
    """
    
    df = df.sort_values('diff', ascending = False)
    
    # Get the head, tail and middle items
    head = df.head(m)
    middle = df.iloc[int(len(df)/2)-int(m/2) : int(len(df)/2) + int(m/2)]
    tail = df.tail(m)

    # Concat the results
    all_results = pd.concat([head, middle, tail])
    
    # Drop not necessary columns
    all_results = all_results.drop(['evaluation', 'evaluation_tmdb'], axis = 1)

    return all_results


def return_figures_tmdb():
    """
    Creates the plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # First plot: Histogram with difference between my evaluation and tmdb    
    df = df_movie_tmdb.copy()

    # Select only the diff-column
    x = df['diff']

    graph_one = [go.Histogram(
        x = x)]

    layout_one = dict(title='Distribution of the difference between TMDBs and my own evaluation',
                    xaxis=dict(title='Difference (absolute)'),
                    yaxis=dict(title='Count')
                    )

    # Second plot: Show items with highest positive and negative difference
    df = me_vs_tmdb_results(df_movie_tmdb, 10)

    color_values = list(range(len(df['title'])))

    graph_two = [go.Bar(
        x = df['diff'],
        y = df['title'], 
        orientation = 'h',
        marker = dict(
            color = color_values,
            colorscale='Viridis'
        )
    )]

    layout_two = dict(title='The movies with the highest positive and negative difference as well as the middle section',
                    xaxis=dict(title='Difference'),
                    yaxis=dict(title='Title'),
                    autosize = True,
                    height = 800)
                  #  bargap = 0.75)



    # append all charts to the figures list
    figures_tmdb = []
    figures_tmdb.append(dict(data=graph_one, layout=layout_one))
    figures_tmdb.append(dict(data=graph_two, layout=layout_two))

    return figures_tmdb




