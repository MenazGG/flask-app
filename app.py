import os
from flask import Flask, render_template

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Career page
@app.route("/career")
def career():
    return render_template("career.html")

# Advice page
@app.route("/advice")
def advice():
    return render_template("advice.html")

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Layout page
@app.route("/layout")
def layout():
    return render_template("layout.html")

# Resources page
@app.route("/resources")
def resources():
    return render_template("resources.html")

# Results page
@app.route("/results")
def results():
    return render_template("results.html")

# Maps page
@app.route("/maps")
def maps():
    return render_template("maps.html")

# Jobs page
@app.route("/jobs")
def jobs():
    return render_template("jobs.html")

# Pathways page
@app.route("/pathways")
def pathways():
    return render_template("pathways.html")

# Questionnaire page
@app.route("/questionnaire")
def questionnaire():
    return render_template("questionnaire.html")

# IRK Notes page
@app.route("/irk_notes")
def irk_notes():
    return render_template("irk_notes.html")

# BM Notes page
@app.route("/bm_notes")
def bm_notes():
    return render_template("bm_notes.html")


# Run server (Render-ready)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)