import pandas as pd
import plotly.graph_objs as go
import altair as alt



# Read in the data from the movie opera diary.
diary_mov_op = pd.read_csv('https://raw.githubusercontent.com/muellermax/movie-opera-diary/master/wrangling_scripts/input.csv')


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


    # Prepare the Altair plot
    chart = alt.Chart(df_grouped).mark_bar(size = 17).encode(
        x='month', # over time
        y='count', # count on y-axis
        color=alt.Color(input_var, scale=alt.Scale(scheme='viridis')), # different colors
        tooltip = [input_var, 'count', 'month'] # tooltips
    ).properties(width=800, height=600)
    
    chart.save('./myapp/templates/items_over_time.json')


show_items_over_time(diary_mov_op, '2017-01-01', 'category')


#### Idee: JSON Grafiken erstellen und dann in index file inkludieren. 
https://www.reddit.com/r/flask/comments/gghoak/does_anyone_have_any_experience_or_examples_with/
https://github.com/vega/vega-embed/blob/master/README.md
https://github.com/dushyantkhosla/flasked-altair