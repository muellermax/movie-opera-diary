import pandas as pd
import numpy as np
import plotly.graph_objs as go

df_movies = pd.read_csv('https://raw.githubusercontent.com/muellermax/movie-opera-diary/master/wrangling_scripts/input_movies.csv')

def show_items_over_time(df, since, input_var):
    """
    Function to show the count of different input_vars over time. 
    
    Input: 
        df (DataFrame): The movie opera diary DataFrame
        since (string): Specify the start date
        input_var (string): Specify the item: 'category', 'place', 'creator'
    
    Output: 
        An Altair plot
    """
    
    # Select DataFrame since a specific date
    df = df[df['date'] >= since]

    # Groupby month and the input_var
    df_grouped = df.groupby(['month', input_var])['title'].count().reset_index()

    # Rename columns
    df_grouped.columns = ['month', input_var, 'count']
    
    return df_grouped


def show_item_vs_count(df, input_var, m):
    """
    A function to visualize count vs. evaluation for any input variable. 
    
    Input: 
        df (DataFrame): The movie opera diary DataFrame
        input_var (string): Choose between 'title', 'company', 'creator', 'place'
        m (int): How many items should be included (e.g. 'Top-30')
        exclude_opera (bool): Choose if operas should be included

    Output: 
        A seaborn scatterplot. 
    """
    # Group df by the input_var and get the values for evaluation and the count
    df_all = df.groupby(input_var).agg(
        {'evaluation': 'mean',
        'date': 'count'}).reset_index().sort_values('date', ascending = False).head(m)

    # Rename columns
    df_all.columns = [input_var, 'evaluation', 'count']
    
    return df_all


def return_figures_movies():
    """
    Creates the plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # Plots categories over time
    graph_one = []

    df = show_items_over_time(df_movies, '2017-01-01', 'category')

    color_values = list(range(df['category'].unique()))

    for item in df['category'].unique():
        df_cat = df[df['category'] == item]
        x_val = df_cat['month']
        y_val = df_cat['count']
        graph_one.append(
            go.Bar(
                x=x_val,
                y=y_val,
                name=item,
                marker = dict(
                        color = color_values,
                        colorscale='Bluered_r'
                             )
                  )
        )

    layout_one = dict(title='Development of movie categories over time',
                      xaxis=dict(title='Date'),
                      yaxis=dict(title='Categories'),
                      barmode='stack'
                      )

    # The second plot shows the 20 most viewed items, their average evaluation and number of views
    graph_two = []

    df = show_item_vs_count(df_movies, 'title', 20)

    for item in df['title'].unique():
        graph_two.append(
            go.Scatter(
                x=df.loc[df['title'] == item, 'count'],
                y=df.loc[df['title'] == item, 'evaluation'],
                mode='markers',
                marker=dict(
                    size=df.loc[df['title'] == item, 'evaluation'],
                    sizemode='area',
                    sizeref=2.*max(df['evaluation'].tolist())/(40.**2),
                    sizemin=4),
                name=item,
                showlegend=False
            )
        )
    
    layout_two = dict(title='The 20 most viewed items',
                    xaxis=dict(title='Number of views'),
                    yaxis=dict(title='Average evaluation')
                    )

    # The third plot shows the 10 most viewed categories, their average evaluation and number of views
    graph_three = []

    df = show_item_vs_count(df_movies, 'category', 10)

    for item in df['category'].unique():
        graph_three.append(
            go.Scatter(
                x=df.loc[df['category'] == item, 'count'],
                y=df.loc[df['category'] == item, 'evaluation'],
                mode='markers',
                marker=dict(
                    size=df.loc[df['category'] == item, 'evaluation'],
                    sizemode='area',
                    sizeref=2.*max(df['evaluation'].tolist())/(40.**2),
                    sizemin=4),
                name=item
            )
        )
    
    layout_three = dict(title='The 10 most viewed categories',
                    xaxis=dict(title='Number of views'),
                    yaxis=dict(title='Average evaluation')
                    )

    # The fourth plot shows the 10 most viewed creators, their average evaluation and number of views
    graph_four = []

    df = show_item_vs_count(df_movies, 'creator', 15)

    for item in df['creator'].unique():
        graph_four.append(
            go.Scatter(
                x=df.loc[df['creator'] == item, 'count'],
                y=df.loc[df['creator'] == item, 'evaluation'],
                mode='markers',
                marker=dict(
                    size=df.loc[df['creator'] == item, 'evaluation'],
                    sizemode='area',
                    sizeref=2.*max(df['evaluation'].tolist())/(40.**2),
                    sizemin=4),
                name=item
           )
         )
    
    layout_four = dict(title='The 15 most viewed directors',
                    xaxis=dict(title='Number of views'),
                    yaxis=dict(title='Average evaluation')
                    )

    # append all charts to the figures list
    figures_movies = []
    figures_movies.append(dict(data=graph_one, layout=layout_one))
    figures_movies.append(dict(data=graph_two, layout=layout_two))
    figures_movies.append(dict(data=graph_three, layout=layout_three))
    figures_movies.append(dict(data=graph_four, layout=layout_four))

    return figures_movies
#### End of 

 