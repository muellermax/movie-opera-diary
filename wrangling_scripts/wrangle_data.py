import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

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
#

def return_figures():
    """Creates the plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    graph_one = []

    df = show_items_over_time(df_movie_op, '2017-01-01', 'category')

    x_val = df['month'].tolist()
    y_val = df['count'].tolist()
    color = df['category'].tolist()

    graph_one.append(
        go.Bar(
            x=x_val,
            y=y_val,
            color=color
        )
    )


    layout_one = dict(title='Daily increase of confirmed cases of Covid-19 in Chile',
                      xaxis=dict(title='Date'),
                      yaxis=dict(title='Confirmed cases'),
                      )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))

    return figures


#### Idee: JSON Grafiken erstellen und dann in index file inkludieren. 
# https://www.reddit.com/r/flask/comments/gghoak/does_anyone_have_any_experience_or_examples_with/
# https://github.com/vega/vega-embed/blob/master/README.md
# https://github.com/dushyantkhosla/flasked-altair


# https://www.geeksforgeeks.org/how-to-create-stacked-bar-chart-in-python-plotly/