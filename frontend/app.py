## from [] import []
## from [] import []
import os
from flask import Flask, jsonify, render_template, request, make_response
from flask_pymongo import PyMongo
import requests
import json
import pandas as pd

from breed_finder import best_breed


app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")
    
@app.route("/findapup")
def input():
    # jessica's python
    return render_template("input.html")

@app.route("/findapup/create-entry", methods=["POST", "GET"])
def create_entry():
    adj_list = []
    dog_size = []

    req = request.get_json()    

    adj_list = req["traits"]

    for k, v in req.items():
        if k =='size':
            dog_size.append(v)

    print(f"Dog size: {dog_size}; Adj: {adj_list}")
    
    # return req

    breed = best_breed(adj_list, dog_size)
    breeds = breed["name"]
    
    best_pup = []
    best_pup.append(breeds[0])
    best_pup.append(breeds[1])
    best_pup.append(breeds[2])
    print(best_pup)
        
    return breeds
    
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

