import pandas as pd
import plotly.graph_objs as go

# Read in the data from the movie opera diary.
diary_mov_op = pd.read_csv('input.csv')

def show_items_over_time(df, since, input_var):
    """
    Function to show the count of different input_vars over time. 
    
    Input: 
        df (DataFrame): The movie opera diary DataFrame
        since (string): Specify the start date
        input_var (string): Specify the item: 'category', 'place', 'creator'
    
    Output: 
        A plotly plot
    """
    
    # Select DataFrame since a specific date
    df = df[df['date'] >= since]

    # Groupby month and the input_var
    df_grouped = df.groupby(['month', input_var])['title'].count().reset_index()

    # Rename columns
    df_grouped.columns = ['month', input_var, 'count']

    return items_over_time_df


def return_figures():
    """Creates plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """




    graph_one = []
    df = show_items_over_time(diary_mov_op, '2017-01-01', 'category')
    x_val = df['month'].tolist()
    y_val = df['count'].tolist()

    graph_one.append(
        go.Bar(
            x=x_val,
            y=y_val,
            name='Confirmed cases',
            hovertemplate='%{y:,.2}'
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
