import os
import pymongo
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from flask import jsonify

# CONN = os.getenv("CONN")
CONN="string"
client = pymongo.MongoClient(CONN)
db = client.austin_dogs
# print(CONN)
# pd.options.display.max_columns = 999

def all_pups():
    all_dogs_data = []
    for i in db.dogs.find():
        all_dogs_data.append({key: value for key, value in i.items() if not key == "_id"})

    # print(all_dogs_data)

    # dog_dict = all_dogs_data.to_dict()

    return jsonify(all_dogs_data)
