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


if __name__ == "__main__":
    app.run(debug=False, port=5001)
