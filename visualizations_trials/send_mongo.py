import os
import pymongo
from request_clean_intakes import clean_intake_data

CONN = os.getenv("CONN")
client = pymongo.MongoClient(CONN)
db = client.austin_dogs

dog_df = clean_intake_data()

dog_dict = dog_df.to_dict("records")

db.dogs.drop()
db.dogs.insert_many(dog_dict)

