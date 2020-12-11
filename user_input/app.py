from flask import jsonify, Flask
# from test_ideas_2 import size, choice, best_breed
# import requests
# import pandas as pd 
from print_raw_data import all_pups
import pymongo
import os
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
#     CONN=string
#     client = pymongo.MongoClient(CONN)
#     db = client.austin_dogs

#     all_dogs_data = []
#     for i in db.dogs.find():
#         all_dogs_data.append({key: value for key, value in i.items() if not key == "_id"})

#     # print(all_dogs_data)

#     # dog_dict = all_dogs_data.to_dict()

    return all_pups()


# @app.route("/choice")
# def user_input():
#     size()
#     choice()
#     best_breed()
#     return best_breed()


@app.route("/all")
def all_dogs():
    return "This works"
    

if __name__ == "__main__":
    app.run(debug = True)
