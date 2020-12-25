from myapp import app
import json, plotly
from flask import render_template
from wrangling_scripts.wrangle_data import return_figures_index
from wrangling_scripts.wrangle_data_tmdb import return_figures_tmdb

@app.route('/')
@app.route('/index.html')
def index():

    figures = return_figures_index()

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
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures_tmdb)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures_tmdb, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('tmdb.html', ids=ids, figuresJSON = figuresJSON)