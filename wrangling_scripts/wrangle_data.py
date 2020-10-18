import pandas as pd
import plotly.graph_objs as go
import altair as alt


# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

# Read in Covid-19 cases and deaths datasets from CSSE at John Hopkins University on Github.
csse_cases_all = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
csse_deaths_all = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

latin_america = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'French', 'Guiana',
                 'Guyana Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']


# Read in the data from the movie opera diary.
diary_mov_op = pd.read_csv('https://raw.githubusercontent.com/muellermax/movie-opera-diary/master/wrangling_scripts/input.csv')

# Function to retrieve data for a single country from the CSSE data.
def single_country(country, df):
    """
    Function to provide Dataframe with cumulated cases of Covid-19
    out of CSSE data for a single country.

    Args:
        country (string): Name of country whose timeline should be prepared.
        df (Dataframe): Name of dataframe (confirmed cases or deaths) that should be included.

    Returns:
        country_timeline (Dataframe): Dataframe with two columns, datetime and confirmed cases.
    """

    # Select rows for the given country and apply pd.melt to unpivot DataFrame
    # from wide to long format. Drop for now unnessary rows ('Province/State', 'Lat', 'Long').
    country_timeline = df[df['Country/Region'] == country]
    country_timeline = country_timeline.drop(['Province/State', 'Country/Region', 'Lat', 'Long'], axis=1)
    country_timeline = pd.melt(country_timeline)
    # country_timeline = country_timeline.drop(country_timeline.index[[0, 1, 2, 3]])

    # Rename columns and apply pandas datetime function.
    country_timeline.columns = ['date', 'cases']
    country_timeline['date'] = country_timeline['date'].astype('datetime64[ns]')

    return country_timeline[country_timeline.cases != 0]


# Function to retrieve data for the daily increase from the CSSE data.
def country_daily(country, df, days=7):
    """
    Function to provide the daily increase of confirmed cases of
    Covid-19 in a chosen country. An extra column includes the rolling
    average for a given amount of days.

    Args:
        country (string): Name of country whose timeline should be prepared.
        days (int), optional: Number of days for rolling average.
        df (Dataframe): Name of dataframe (confirmed cases or deaths) that should be included.

    Returns:
        Dataframe with three columns: date, daily increase and rolling average.
    """

    # Apply single_country_confirmed function and retrieve difference between
    # two dates. Add one column with rolling average and finally fill NaNs will 0.
    country_df = single_country(country, df)
    country_df['cases'] = country_df.cases.diff()

    confirmed_cases_series = country_df.cases
    country_df['rolling_avg'] = confirmed_cases_series.rolling(days).mean()

    country_df.columns = ['date', 'daily increase', 'rolling_avg']

    return country_df.fillna(0)



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
    
    chart.save('items_over_time.json')


def return_figures():
    show_items_over_time(diary_mov_op, '2017-01-01', 'category')

