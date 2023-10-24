import os

from flask import Flask, render_template


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