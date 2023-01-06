from flask import Flask, render_template
from os import listdir

app = Flask(__name__)

@app.route("/")
def gallery():
    files = listdir(app.static_folder)
    files.sort()

    return render_template('gallery.html', static_url_path=app.static_url_path, files=files)
