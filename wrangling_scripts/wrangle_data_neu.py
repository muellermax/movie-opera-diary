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
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots daily increase of Covid-19 infections in Chile and rolling average.
    # as a line chart

    # First plot
    graph_one = []
    df = show_items_over_time(diary_mov_op, '2017-01-01', 'category')
    x_val = df['month'].tolist()
    y_val = df['count'].tolist()

    graph_one.append(
        go.Bar(
            x=x_val,
            y=y_val
        )
    )

    layout_one = dict(title='Daily increase of confirmed cases of Covid-19 in Chile',
                      xaxis=dict(title='Date'),
                      yaxis=dict(title='Confirmed cases'),
                      barmode='stack'
                      )


    # second chart plots daily increase of Covid-19 deaths in Chile and rolling average.
    graph_two = []
    df = country_daily('Chile', csse_deaths_all)
    x_val = df.date.tolist()
    y_val = df['daily increase'].tolist()

    graph_two.append(
        go.Bar(
            x=x_val,
            y=y_val,
            name='Confirmed deaths',
            hovertemplate='%{y:,.2}'
        )
    )

    y_val2 = df.rolling_avg.tolist()

    graph_two.append(
        go.Scatter(
            x=x_val,
            y=y_val2,
            mode='lines',
            name='Rolling Average',
            hovertemplate='%{y:,.2r}'
        )
    )

    layout_two = dict(title='Daily increase of deaths caused by Covid-19 in Chile',
                      xaxis=dict(title='Date', ),
                      yaxis=dict(title='Deaths'),
                      )

    # third chart plots confirmed cases in South America
    graph_three = []

    for country in latin_america:
        df = single_country(country, csse_cases_all)
        x_val = df.date.tolist()
        y_val = df.cases.tolist()

        graph_three.append(
            go.Scatter(
                x=x_val,
                y=y_val,
                mode='lines',
                name=country,
                hovertemplate='%{y:,.2}'

            )
        )

    layout_three = dict(title='Total confirmed cases of Covid-19 in South America',
                        xaxis=dict(title='Date'),
                        yaxis=dict(title='Confirmed cases (log scale)',
                                   type='log')
                        )

    # Fourth chart plots deaths caused by Covid-19 in South America

    graph_four = []

    for country in latin_america:
        df = single_country(country, csse_deaths_all)
        x_val = df.date.tolist()
        y_val = df.cases.tolist()

        graph_four.append(
            go.Scatter(
                x=x_val,
                y=y_val,
                mode='lines',
                name=country,
                hovertemplate='%{y:,.2}'

            )
        )

    layout_four = dict(title='Total deaths caused by Covid-19 in South America',
                       xaxis=dict(title='Date'),
                       yaxis=dict(title='Deaths caused by Covid-19 (log scale)',
                                  type='log')
                       )

    # Fifth chart is a single value showing the total amount of cases in Chile and the increase.

    df = single_country('Chile', csse_cases_all)
    graph_five = go.Figure(go.Indicator(
                 title={'text': 'Covid-19 cases in Chile'},
                 mode='number+delta',
                 value=df.iloc[-1, 1],
                 delta={'position': "top",
                        'reference': df.iloc[-2, 1],
                        'increasing': {'color': '#8b0000'},
                        'valueformat': '{,}'},
                 number={'valueformat': '{,}'})
                 )

    # Sixths chart is a single value showing the total amount of deaths in Chile and the increase.

    df = single_country('Chile', csse_deaths_all)
    graph_six = go.Figure(go.Indicator(
                 title={'text': 'Covid-19 deaths in Chile'},
                 mode='number+delta',
                 value=df.iloc[-1, 1],
                 delta={'position': "top",
                        'reference': df.iloc[-2, 1],
                        'increasing': {'color': '#8b0000'},
                        'valueformat': '{,}'},
                 number={'valueformat': '{,}'})
                 )


    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    figures.append(dict(data=graph_five))
    figures.append(dict(data=graph_six))

    return figures