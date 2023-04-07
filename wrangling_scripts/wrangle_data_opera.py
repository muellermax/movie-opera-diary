import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px

df_operas = pd.read_csv('https://raw.githubusercontent.com/muellermax/movie-opera-diary/master/wrangling_scripts/input_operas.csv')

colorway_diary = px.colors.qualitative.Prism

def show_items_over_time(df, since, input_var):
    """
    Function to show the count of different input_vars over time. 
    
    Input: 
        df (DataFrame): The movie opera diary DataFrame
        since (string): Specify the start date
        input_var (string): Specify the item: 'category', 'place', 'creator'
    
    Output: 
        df_grouped (DataFrame): The DataFrame grouped by the input_var and the total count of the items
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

    Output: 
        A seaborn scatterplot. 
    """
    # Group df by the input_var and get the values for evaluation and the count
    df_all = df.groupby(input_var).agg(
        {'evaluation': 'mean',
        'date': 'count'}).reset_index().round(2).sort_values('date', ascending = False).head(m)

    # Rename columns
    df_all.columns = [input_var, 'evaluation', 'count']
    
    return df_all


def knowing_the_creators_oevre(df):
    """
    A function that allows me to show how I evaluated the creators whole oevre and
    shows me which creators I evaluate best over the total oevre - there are some
    creators who have a few operas that I have evaluated extremely good and other 
    operas not so good. 

    Input: 
        df (DataFrame): The DataFrame with the opera data
    
    Output: 
        knowing_the_directors_oevre (DataFrame): A DataFrame with the mean 
        evaluation and the number of unique views
    """

    # Groupby creator and title, to get the mean evaluation for each item. 
    df = df.groupby(['creator', 'title']).agg({
            'date': 'count',
            'evaluation': 'mean'
        }).reset_index()

    # Now Groupby creator to get the overall overview
    df = df.groupby(['creator']).agg({
            'title': 'nunique',
            'evaluation': 'mean'
        }).reset_index()

    # Return the DataFrame
    return df.round(2).sort_values('title', ascending = False).head(10)



def return_figures_opera():
    """
    Creates the plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # Plots categories over time
    graph_one = []

    df = show_items_over_time(df_operas, '2017-01-01', 'place')

    for item in df['place'].unique():
        df_cat = df[df['place'] == item]
        x_val = df_cat['month']
        y_val = df_cat['count']
        graph_one.append(
            go.Bar(
                x=x_val,
                y=y_val,
                name=item
            )
        )

    layout_one = dict(title='Visit of different opera sites',
                      xaxis=dict(title='Date'),
                      yaxis=dict(title='Opera'),
                      barmode='stack',
                      colorway = colorway_diary,
                      hoverlabel = dict(
                        namelength = -1 # To show the whole label name
                      ),
                      plot_bgcolor = '#E8E8E8'
                      )

    # The second plot shows the 20 most viewed items, their average evaluation and number of views
    graph_two = []

    df = show_item_vs_count(df_operas, 'title', 15)

    for item in df['title'].unique():
        graph_two.append(
            go.Scatter(
                x=df.loc[df['title'] == item, 'count'].tolist(),
                y=df.loc[df['title'] == item, 'evaluation'].tolist(),
                mode='markers',
                marker=dict(
                    size=df.loc[df['title'] == item, 'evaluation'].tolist(),
                    sizemode='area',
                    sizeref=2.*max(df['evaluation'].tolist())/(40.**2),
                    sizemin=4),
                name=item,
                showlegend=False
            )
        )
    
    layout_two = dict(title='The 15 most viewed items',
                    xaxis=dict(title='Number of views'),
                    yaxis=dict(title='Average evaluation'),
                    colorway = colorway_diary,
                      hoverlabel = dict(
                        namelength = -1 # To show the whole label name
                      ),
                      plot_bgcolor = '#E8E8E8'
                    )

    # The third plot shows the 10 most viewed categories, their average evaluation and number of views
    graph_three = []

    df = show_item_vs_count(df_operas, 'place', 10)

    for item in df['place'].unique():
        graph_three.append(
            go.Scatter(
                x=df.loc[df['place'] == item, 'count'].tolist(),
                y=df.loc[df['place'] == item, 'evaluation'].tolist(),
                mode='markers',
                marker=dict(
                    size=df.loc[df['place'] == item, 'evaluation'].tolist(),
                    sizemode='area',
                    sizeref=2.*max(df['evaluation'].tolist())/(40.**2),
                    sizemin=4),
                name=item
            )
        )
    
    layout_three = dict(title='The most visited places',
                    xaxis=dict(title='Number of visits'),
                    yaxis=dict(title='Average evaluation'),
                    colorway = colorway_diary,
                      hoverlabel = dict(
                        namelength = -1 # To show the whole label name
                      ),
                      plot_bgcolor = '#E8E8E8'
                    )

    # The fourth plot shows the 10 most viewed creators, their average evaluation and number of views
    graph_four = []

    df = show_item_vs_count(df_operas, 'creator', 15)

    for item in df['creator'].unique():
        graph_four.append(
            go.Scatter(
                x=df.loc[df['creator'] == item, 'count'].tolist(),
                y=df.loc[df['creator'] == item, 'evaluation'].tolist(),
                mode='markers',
                marker=dict(
                    size=df.loc[df['creator'] == item, 'evaluation'].tolist(),
                    sizemode='area',
                    sizeref=2.*max(df['evaluation'].tolist())/(40.**2),
                    sizemin=4),
                name=item
           )
         )
    
    layout_four = dict(title='The 15 most viewed composers',
                    xaxis=dict(title='Number of views'),
                    yaxis=dict(title='Average evaluation'),
                    colorway = colorway_diary,
                      hoverlabel = dict(
                        namelength = -1 # To show the whole label name
                      ),
                      plot_bgcolor = '#E8E8E8'
                    )


    # The sixth plot shows the evaluation for each unique mopera for each creator
    graph_five = []

    df = knowing_the_creators_oevre(df_operas)
    
    for item in df['creator'].unique():
        graph_five.append(
            go.Scatter(
                x=df.loc[df['creator'] == item, 'title'],
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

    layout_five = dict(title='Views of different movies for each Director',
                    xaxis=dict(title='Number of unique items'),
                    yaxis=dict(title='Average evaluation'),
                    colorway = colorway_diary,
                        hoverlabel = dict(
                        namelength = -1 # To show the whole label name
                        ),
                        plot_bgcolor = '#E8E8E8'
                    )




    # append all charts to the figures list
    figures_opera = []
    figures_opera.append(dict(data=graph_one, layout=layout_one))
    figures_opera.append(dict(data=graph_two, layout=layout_two))
    figures_opera.append(dict(data=graph_three, layout=layout_three))
    figures_opera.append(dict(data=graph_four, layout=layout_four))
    figures_opera.append(dict(data=graph_five, layout=layout_five))

    return figures_opera
