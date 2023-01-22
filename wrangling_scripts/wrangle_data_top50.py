import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px

df_movies = pd.read_csv('https://raw.githubusercontent.com/muellermax/movie-opera-diary/master/wrangling_scripts/input_movies.csv', encoding = "UTF-8")

df_movies_tmdb = pd.read_csv('https://raw.githubusercontent.com/muellermax/movie-opera-diary/master/wrangling_scripts/input_tmdb.csv', encoding = "UTF-8")

