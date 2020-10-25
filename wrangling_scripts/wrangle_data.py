import pandas as pd
import plotly.graph_objs as go

df_movie_op = pd.read_csv('https://raw.githubusercontent.com/muellermax/movie-opera-diary/master/wrangling_scripts/input.csv')

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


def return_figures():
    """
    Creates the plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # Plots categories over time
    graph_one = []

    df = show_items_over_time(df_movie_op, '2017-01-01', 'category')

    for item in df['category'].unique():
        df_cat = df[df['category'] == item]
        x_val = df_cat['month'].tolist()
        y_val = df_cat['count']
        graph_one.append(
            go.Bar(
                x=x_val,
                y=y_val,
                name=item,
                marker={'color': (df['category'].unique()).tolist().index(name),
                'colorscale': 'Viridis'}
            )
        )

    layout_one = dict(title='Development of movie and opera categories over time',
                      xaxis=dict(title='Date'),
                      yaxis=dict(title='Categories'),
                      barmode='stack'
                      )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))

    return figures