# from best_one_so_far import size, choice, best_breed
# from [] import []
import os
from flask import Flask, jsonify, render_template, request, make_response
# from flask_pymongo import PyMongo
from size_v2 import best_breed
import json
import pandas as pd

adj_list = []
dog_size = []

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/findapup")
def input():
    # adj_list = ['smart', 'spunky', 'loyal', 'brave', 'bold', 'protective', 'sweet', 'trainable']
    # dog_size = ['medium']
    return best_breed(adj_list, dog_size)
    
    return render_template("input.html")


@app.route("/findapup/create-entry", methods=["POST", "GET"])
def create_entry():

    req = request.get_json()
    
    for k, v in req.items():
        print(k, v)

    for k, v in req.items():
        if v =='Yes':
            adj_list.append(k)

    for k, v in req.items():
        if k =='name':
            dog_size.append(v)

    print(f"dog size is {dog_size} and adj are {adj_list}")
    return req




if __name__ == "__main__":
    app.run(debug=True)