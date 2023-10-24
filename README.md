# Movie APP
#### Video Demo:  <https://www.youtube.com/watch?v=D75Pr0pGz_c>
#### Description:
This application uses FetchApi to display content from The MovieDB. There are 20 different tabs for each genre. Each tab pulls an array of 20 of the daily top ranking movies. It changes and updates daily. The user has the ability to search for certin movies. The app displays the searched movie and any other movies with that search term.

![Homepage of Movie App](static/images/homepage.png)

## Files:
### **Root Folder**
README file<br>
App.py
```
    import os

    from flask import Flask, render_template
    from flask_session import Session

    app = Flask(__name__)

    @app.route("/")
    def trending():
        return render_template("index.html")

    @app.route("/action")
    def action():
        return render_template("action.html")

    @app.route("/adventure")
    def adventrue():
        return render_template("adventure.html")

    @app.route("/animation")
    def animation():
        return render_template("animation.html")

    @app.route("/comedy")
    def comedy():
        return render_template("comedy.html")

    @app.route("/crime")
    def crime():
        return render_template("crime.html")

    @app.route("/documentary")
    def documentry():
        return render_template("documentary.html")

    @app.route("/drama")
    def drama():
        return render_template("drama.html")

    @app.route("/family")
    def family():
        return render_template("family.html")

    @app.route("/fantasy")
    def fantasy():
        return render_template("fantasy.html")

    @app.route("/history")
    def history():
        return render_template("history.html")

    @app.route("/horror")
    def horror():
        return render_template("horror.html")

    @app.route("/music")
    def music():
        return render_template("music.html")

    @app.route("/mystery")
    def mystery():
        return render_template("mystery.html")

    @app.route("/romance")
    def romance():
        return render_template("romance.html")

    @app.route("/sciencefiction")
    def sciencefiction():
        return render_template("sciencefiction.html")

    @app.route("/thriller")
    def thriller():
        return render_template("thriller.html")

    @app.route("/tvmovie")
    def tvmovie():
        return render_template("tvmovie.html")

    @app.route("/war")
    def war():
        return render_template("war.html")

    @app.route("/western")
    def western():
        return render_template("western.html")
```


### **Templetes Folder**
>layout.html<br>
```
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="../static/styles.css">
            <title>Movie App</title>
        </head>
        <body>
            <header>
                <form id="form" class="form">
                    <input type="text" autocomplete="off" placeholder="Search here" id="search" class="search">
                </form>
            </header>

            {% block h1 %}{% endblock %}
            <nav>
                <ul>
                    <li class="active"><a href="/">Trending</a></li>
                    <li class="active"><a href="/action">Action</a></li>
                    <li class="active"><a href="/adventure">Adventure</a></li>
                    <li class="active"><a href="/animation">Animation</a></li>
                    <li class="active"><a href="/comedy">Comedy</a></li>
                    <li class="active"><a href="/crime">Crime</a></li>
                    <li class="active"><a href="/documentary">Documentary</a></li>
                    <li class="active"><a href="/drama">Drama</a></li>
                    <li class="active"><a href="/family">Family</a></li>
                    <li class="active"><a href="/fantasy">Fantasy</a></li>
                    <li class="active"><a href="/history">History</a></li>
                    <li class="active"><a href="/horror">Horror</a></li>
                    <li class="active"><a href="/music">Music</a></li>
                    <li class="active"><a href="/mystery">Mystery</a></li>
                    <li class="active"><a href="/romance">Romance</a></li>
                    <li class="active"><a href="/sciencefiction">Science Fiction</a></li>
                    <li class="active"><a href="/thriller">Thriller</a></li>
                    <li class="active"><a href="/tvmovie">TV Movie</a></li>
                    <li class="active"><a href="/war">War</a></li>
                    <li class="active"><a href="/western">Western</a></li>
                </ul>
            </nav>

                <div class="moviemaincontainer" id="moviemaincontainer">
                    <div class="moviemain">
                        <img src="../static/images/movie.png" alt="">
                        <div class="title">
                            <h3>Title</h3>
                        </div>
                        <div class="movie-overview">
                            <p>
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet veritatis eligendi hic enim, accusamus vel iste commodi vitae quam, reiciendis in repellendus. Blanditiis ipsa aut sequi nam porro ullam itaque!
                            </p>
                        </div>
                    </div>

                    <div class="moviemain">
                        <img src="../static/images/movie.png" alt="">
                        <div class="title">
                            <h3>Title</h3>
                        </div>
                        <div class="movie-overview">
                            <p>
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet veritatis eligendi hic enim, accusamus vel iste commodi vitae quam, reiciendis in repellendus. Blanditiis ipsa aut sequi nam porro ullam itaque!
                            </p>
                        </div>
                    </div>

                    <div class="moviemain">
                        <img src="../static/images/movie.png" alt="">
                        <div class="title">
                            <h3>Title</h3>
                        </div>
                        <div class="movie-overview">
                            <p>
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet veritatis eligendi hic enim, accusamus vel iste commodi vitae quam, reiciendis in repellendus. Blanditiis ipsa aut sequi nam porro ullam itaque!
                            </p>
                        </div>
                    </div>

                    <div class="moviemain">
                        <img src="../static/images/movie.png" alt="">
                        <div class="title">
                            <h3>Title</h3>
                        </div>
                        <div class="movie-overview">
                            <p>
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet veritatis eligendi hic enim, accusamus vel iste commodi vitae quam, reiciendis in repellendus. Blanditiis ipsa aut sequi nam porro ullam itaque!
                            </p>
                        </div>
                    </div>

                    <div class="moviemain">
                        <img src="../static/images/movie.png" alt="">
                        <div class="title">
                            <h3>Title</h3>
                        </div>
                        <div class="movie-overview">
                            <p>
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet veritatis eligendi hic enim, accusamus vel iste commodi vitae quam, reiciendis in repellendus. Blanditiis ipsa aut sequi nam porro ullam itaque!
                            </p>
                        </div>
                    </div>


                </div>

            {% block script %}{% endblock %}

        </body>
    </html>
```
>index.html<br>
action.html<br>
adventure.html<br>
animation.html<br>
comedy.html<br>
crime.html<br>
documentary.html<br>
drama.html<br>
family.html<br>
fantasy.html<br>
history.html<br>
horror.html<br>
index.html<br>
layout.html<br>
music.html<br>
mystery.html<br>
romance.html<br>
sciencefiction.html<br>
thriller.html<br>
tvmovie.html<br>
war.html<br>
western.html<br>

ALL of the html files extends the layout.html file. The only changes made is the heading and the link to the Javascript file.
```
{% extends "layout.html" %}

{% block h1 %}
    <div id="mainh1" class ="mainh1">
        <h1>Trending Movies</h1>
    </div>
{% endblock %}



{% block script %}
    <script src="../static/script.js"></script>
{% endblock %}
```

### **Script Folder**

### **Static Folder**
_holds the image folder, stylesheet, and Javascript files_<br>
>action.js<br>
adventure.js<br>
animation.js<br>
comedy.js<br>
crime.js<br>
documentary.js<br>
drama.js<br>
family.js<br>
fantasy.js<br>
history.js<br>
horror.js<br>
music.js<br>
mystery.js<br>
romance.js<br>
sciencefiction.js<br>
script.js<br>
styles.css
thriller.js<br>
tvmovie.js<br>
war.js<br>
western.js<br>
```
    const apiKey = "625a71e3573f2ad27738f7b6ccd532ed";
    const baseUrl = "https://api.themoviedb.org/3";
    const apiURL = baseUrl + "/discover/movie?" + `api_key=${apiKey}&with_genres=28`;
    const imgPosterUrl = "https://image.tmdb.org/t/p/original";
    const mainTag = document.getElementById("moviemaincontainer");
    const searchH1 = document.getElementById("mainh1")
    const form = document.getElementById("form");
    const search = document.getElementById("search")
    const searchURL = baseUrl + "/search/movie?";

    console.log(apiURL)

    getMovies(apiURL);

    function getMovies(url) {
        fetch(url).then(res => res.json()).then(data => {
            console.log(data.results)
            showMovies(data.results);
        });
    }

    function showMovies(data) {
        moviemaincontainer.innerHTML = "";
        data.forEach(movie => {
            const {title, poster_path, overview} = movie;
            const movieE1 = document.createElement('div');
            movieE1.classList.add("movie");
            movieE1.innerHTML = `
            <div class="moviemain">
                <img src="${imgPosterUrl + poster_path}" alt="${title}">
                <div class="title">
                    <h3>${title}</h3>
                </div>
                <div class="movie-overview">
                    <p>${overview}</p>
                </div>
            `
            moviemaincontainer.appendChild(movieE1);
        })
    }

    //event listener for when button clicked
    form.addEventListener("submit", (e) => {
        e.preventDefault();

        mainh1.innerHTML ="";

        let searchTerm = search.value;
        const newH1 = document.createElement('div');

        if(searchTerm) {
            getMovies(searchURL+"query="+searchTerm + `&api_key=${apiKey}`);
            mainh1.innerHTML =`
            <div class ="mainh1">
                <h1>Movies Titled: ${searchTerm}</h1>
            </div>
            `
            mainh1.appendChild(newH1)

        }
    })
```

All of the javascript files uses the same layout, the only difference is that the api link is different for each genre.


