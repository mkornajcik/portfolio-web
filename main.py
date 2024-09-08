from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
import os

app = Flask(__name__, template_folder="template")
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
ckeditor = CKEditor(app)
Bootstrap5(app)

color = "#f04752"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
