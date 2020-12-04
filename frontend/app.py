## from [] import []
## from [] import []
import os
from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")
    
@app.route("/findapup")
def input():
    # jessica's python
    return render_template("input.html")
    
@app.route("/results")
def results():
    # return render_template("results.html")
    return "and this one!"


@app.route("/justforfun")
def for_fun():
    # return render_template("fun.html")
    return "ditto"

if __name__ == "__main__":
    app.run(debug=True)

