# from best_one_so_far import size, choice, best_breed
# from [] import []
import os
from flask import Flask, jsonify, render_template, request, make_response
# from flask_pymongo import PyMongo
from size_v2 import best_breed
import json
import pandas as pd
import requests

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
    
    # for k, v in req.items():
    #     print(k, v)

    # for k, v in req.items():
    #     if v =='Yes':
    #         adj_list.append(k)
    

    # -------vvv-------Reynolds Code-------vvv-------
    adj_list = req["traits"]

    # -------^^^-------Reynolds Code-------^^^-------

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




if __name__ == "__main__":
    app.run(debug=True)