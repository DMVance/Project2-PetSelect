## from [] import []
## from [] import []
import os
from flask import Flask, jsonify, render_template, request, make_response
from flask_pymongo import PyMongo
import requests
import json
import pandas as pd

from breed_finder import best_breed
from dog_search import combined_queries, all_dogs


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/findapup")
def input():
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


@app.route("/findapup/mongo-query", methods=["POST", "GET"])
def mongo_query():

    req = request.get_json()    

    search_breed = req["search_breed"]
    youngest_yrs = req["youngest_yrs"]
    youngest_mos = req["youngest_mos"]
    oldest_yrs = req["oldest_yrs"]
    oldest_mos = req["oldest_mos"]
    search_sex = req["search_sex"]
    search_color = req["search_color"]
    search_injured = req["search_injured"]

    print("Search parameters: ")
    print(search_breed, youngest_yrs, youngest_mos, oldest_yrs, oldest_mos, search_sex, search_color, search_injured)
    

    dogs_df = combined_queries(
        search_breed, 
        youngest_yrs, 
        youngest_mos, 
        oldest_yrs, 
        oldest_mos, 
        search_sex, 
        search_color, 
        search_injured
    )

    columns = [
        "name",
        "sex", 
        "primary_breed", 
        "secondary_breed", 
        "primary_color", 
        "secondary_color", 
        "age_years", 
        "age_months", 
        "age_days", 
        "intake_condition"
        ]

    dogs_df = dogs_df[columns]
    dogs_dicts = dogs_df.to_dict("records")
    dogs_json = json.dumps(dogs_dicts)

    print(type(dogs_json))
    print(dogs_json)
        
    return dogs_json

    
# @app.route("/all-dogs")
# def all_dogs():
#     # return render_template("all_dogs.html")
#     return "and this one!"


# @app.route("/visualizations")
# def for_fun():
#     # return render_template("visualizations.html")
#     return "same here"

# dogs_df = all_dogs()
# dogs_df = dogs_df[columns]
# dogs_dicts = dogs_df.to_dict("records")
# dogs_json = json.dumps(dogs_dicts)
# save to file and reference file in app.js



@app.route("/fun")
def fun():
    return render_template("fun.html")



if __name__ == "__main__":
    app.run(debug=True)

