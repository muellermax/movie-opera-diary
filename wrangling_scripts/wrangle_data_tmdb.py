import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px

df_movie_tmdb = pd.read_csv('https://raw.githubusercontent.com/muellermax/movie-opera-diary/master/wrangling_scripts/input_tmdb.csv')

colorway_diary = px.colors.qualitative.Prism

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
    
    df = df.sort_values('diff', ascending = True)
    
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
    # First plot: Scatterplot with my evaluation vs. TMDB evaluation
    df = df_movie_tmdb.copy()

    # Select the relevant columns
    df = df[['title', 'views', 'evaluation', 'evaluation_tmdb', 'primary genre']]

    graph_one = []

    for item in df['primary genre'].unique():
        graph_one.append(
            go.Scatter(
            x = df.loc[df['primary genre'] == item, 'evaluation'],
            y = df.loc[df['primary genre'] == item, 'evaluation_tmdb'],
            name = item,
            mode = 'markers',
            marker = dict(
                    size = df.loc[df['primary genre'] == item, 'views'])
                        )
            )




    layout_one = dict(title='Development of movie categories over time',
                    xaxis=dict(title='Date'),
                    yaxis=dict(title='Count'),
                    colorway = colorway_diary,
                    plot_bgcolor = '#E8E8E8',
                    hoverlabel = dict(
                    namelength = -1 # To show the whole label name
                    )
                    )


    # Second plot: Histogram with difference between my evaluation and tmdb    
    df = df_movie_tmdb.copy()

    # Select only the diff-column
    x = df['diff']

    bins = 60
    color_values_hist = list(range(bins))

    graph_two = [go.Histogram(
        x = x,
        nbinsx = bins,
        marker = dict(
            color = color_values_hist,
            cmin = color_values_hist[10],
            cmax = color_values_hist[30],
            colorscale = 'Bluered_r'
        ))]

    layout_two = dict(title='Distribution of the difference between TMDBs and my own evaluation',
                    xaxis=dict(title='Difference (absolute)'),
                    yaxis=dict(title='Count'),
                      plot_bgcolor = '#E8E8E8'
                    )

    # Third plot: Show items with highest positive and negative difference
    df = me_vs_tmdb_results(df_movie_tmdb, 10)

    # Set number of colors for colorscale
    color_values = list(range(len(df['title'])))

    graph_three = [go.Bar(
        x = df['diff'],
        y = df['title'], 
        orientation = 'h',
        marker = dict(
            color = color_values,
            colorscale='Bluered_r'
        ),
        textposition = 'outside',
        cliponaxis = False
    )]

    layout_three = dict(title='The movies with the highest positive and negative difference',
                    xaxis=dict(title='Difference'),
                    yaxis=dict(title= dict(
                        title = 'Title',
                        standoff = 0.5)
                                ),
                    autosize = True,
                    height = 800,
                    margin = dict(
                        l = 400 # Marging on the yaxis (left side)
                                ),
                    hoverlabel = dict(
                        namelength = -1 # To show the whole label name
                                      ),
                      plot_bgcolor = '#E8E8E8'
                    )

    # append all charts to the figures list
    figures_tmdb = []
    figures_tmdb.append(dict(data=graph_one, layout=layout_one))
    figures_tmdb.append(dict(data=graph_two, layout=layout_two))
    figures_tmdb.append(dict(data=graph_three, layout=layout_three))

    return figures_tmdb




