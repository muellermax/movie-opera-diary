from myapp import app
import json, plotly
from flask import render_template
from wrangling_scripts.wrangle_data_movies import return_figures_movies
from wrangling_scripts.wrangle_data_tmdb import return_figures_tmdb

@app.route('/')
@app.route('/index.html')
def index():

    figures = return_figures_movies()

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', 
                           ids=ids,
                           figuresJSON=figuresJSON)

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
    ids_opera = ['figure-{}'.format(i) for i, _ in enumerate(figures_tmdb)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON_opera = json.dumps(figures_opera, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('opera.html', ids=ids_opera, figuresJSON = figures_opera)