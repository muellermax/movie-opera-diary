from myapp import app
import json, plotly
from flask import render_template
from wrangling_scripts.wrangle_data_movies import return_figures_movies
from wrangling_scripts.wrangle_data_tmdb import return_figures_tmdb
from wrangling_scripts.wrangle_data_opera import return_figures_opera

@app.route('/')
@app.route('/index.html')
def index():

    figures_movies = return_figures_movies()

    # plot ids for the html id tag
    ids_movies = ['figure-{}'.format(i) for i, _ in enumerate(figures_movies)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON_movies = json.dumps(figures_movies, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', 
                           ids=ids_movies,
                           figuresJSON=figuresJSON_movies)

@app.route('/')
@app.route('/tmdb.html')
def tmdb():

    figures_tmdb = return_figures_tmdb()

    # plot ids for the html id tag
    ids_tmdb = ['figure-{}'.format(i) for i, _ in enumerate(figures_tmdb)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON_tmdb = json.dumps(figures_tmdb, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('tmdb.html', ids=ids_tmdb, figuresJSON = figuresJSON_tmdb)


@app.route('/')
@app.route('/opera.html')
def opera():

    figures_opera = return_figures_opera()

    # plot ids for the html id tag
    ids_opera = ['figure-{}'.format(i) for i, _ in enumerate(figures_opera)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON_opera = json.dumps(figures_opera, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('opera.html', ids=ids_opera, figuresJSON = figures_opera)