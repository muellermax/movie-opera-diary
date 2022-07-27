# The movie and opera diary

## Index

1. [About the project and my own data](#about)
2. [Data](#data)
3. [Access](#access)
4. [Findings](#findings)
4. [File descriptions](#file-description)
5. [How to interact](#interact)
6. [Acknowledgements](#thx)
7. [Author](#author)
8. [License](#license)
 
## <a class="anchor" id = "about">About the project and my own data</a>

Two of my favorite hobbies are watching movies and going to the opera. Inspired by some friends who had good old analogue diaries, I started writing down some data every time 
I watched a movie or went to the opera. First I used a Word document, but changed to Excel very soon (wise choice). The data I currently gather is as follows: 
1. date
2. title (normally the original title as in IMDB)
3. creator (the director or with operas the composer)
4. release year (first release, which is important to parse the data with the TMDB data)
5. place (which cinema, which opera, etc.)
6. company (who was with me; this information does not appear in my dashboards, Datenschutz you know ;))
7. category (Netflix, Blu Ray, cinema, etc.)
8. evaluation (my own evaluation between 0 and 100)
9. imdb_id (I had a phase where I stored every IMDB ID, but this was to much work)
10. comment (sometimes I write some thoughts about the movie or opera of if it was some special occasion)

Apart from movies and operas I also gather information about books and concerts. I even started to write down new Whiskeys I tried but it seems that I am not a sufficiently heavy drinker for this... 

After doing some Data Science courses in Codecademy and Udacity, I first analyzed my diary with a Jupyter Notebook and decided then - after learning about Web-Development - that I should make a dashboard. 


## <a class="anchor" id = "data">Data</a>

Additional to my own data (see above), I have currently the following external data sources: 
* [The Movie Databaes (TMDB)](https://www.themoviedb.org/): A community built database since 2008. I access TMDB over [their own API](https://www.themoviedb.org/documentation/api) using a very practical [wrapper](https://pypi.org/project/tmdbsimple/).

I plan to add more data sources for some recommender engines and will update this list. 


## <a class="anchor" id="access">Access</a>

You can have a look at the dashboard via https://movie-opera-diary.herokuapp.com.

Currently I have three subpages: 
* Movie diary: It shows how many movies I watched in which category since the beginning of 2017. 
* Me vs. TMDB: It shows the differences between my evaluation and the TMDB community. 
* Opera diary: The operas I saw and their composers. 
* Top 50: Showing the 50 movies with the highest evaluation. 


## <a class="anchor" id="findings">Findings</a>

<u>Movie diary</u>

* Clearly I have watched a lot of movies at home during March, April and December 2020 (Corona-time). 
* My movie selection in airplanes I not the best and it makes sense: Normally I prefer to watch some easy and entertaining movies during long flights (Marvel, Pixar). Furthermore, I watch movies in airplanes that I would probably not watch at home or pay for them in the cinema. 
* Considering the three main streaming platforms (Netflix, Mubi and Amazon Prime), I watch most stuff on Netflix, but the average evaluation is highest on Amazon Prime and Mubi. 
+ Peter Jackson, Christopher Nolan and Quentin Tarantino are some directors that I could watch every week. I think this is clear in the stats. 

<u>Me vs. TMDB</u>

* I tend to evaluate the movies slightly better than the TMDB community. 
* With some of my favorite movies (The Host, Cherry Blossoms) I am much more generous than the TMDB community. 


<u>Opera diary</u>

* I see a lot of Wagner and Verdi operas.
* Unfortunately, here is missing a lot of data from 2003 until 2013, which were also very heavy opera years. 


## <a class="anchor" id="file-description">File description</a>

The webapp relies on some files that make up the environment for it using Flask and Gunicorn: 
* init, myapp and routes: Initiate the Flask app and render the html templates with the plots as JSON data. 
* wrangel_data_movies/tmdb/opera: Data wrangling files that prepare the data and return Plotly graph objects
* CSV-files: These files are exports from the original diary with a few changes (e.g. without the company information)


## <a class="anchor" id="interact">How to interact</a>

Every idea or contribution is welcome. My next project will be to design a recommender.


## <a class="anchor" id="thx">Acknowledgements</a>

Thanks to the following packages or service providers: 
* [The TMDB community](https://www.themoviedb.org/), especially for providing an easy to use API. 
* [The already mentioned TMDB API wrapper](https://www.themoviedb.org/) by [Celiao](https://github.com/celiao), which I use to access the TMDB database.
* [Derek Eders](https://github.com/derekeder) tutorial about [converting CSV to HTML tables](https://github.com/derekeder/csv-to-html-table) helped me a lot when 
preparing the tables. 
* Of course, without Github, Heroku and Stackoverflow, the dashboard would not exist. 


## <a class="anchor" id="author">Author</a>
Maximilian Müller, Senior Business Development Manager for Smart Metering and Data Analytics in the Renewable Energy sector. Now diving into the field of Data Science.


## <a class="anchor" id="license">License</a>

Copyright 2021 Maximilian Müller

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.