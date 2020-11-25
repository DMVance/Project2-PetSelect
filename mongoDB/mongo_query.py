import os
import pymongo
import pandas as pd

CONN = os.getenv("CONN")
client = pymongo.MongoClient(CONN)
db = client.austin_dogs


# turns mongoDB back into a dataframe (probably should not do this)
# takes several seconds to query and download the whole db
# question for ed: should we be just querying the db with pymongo
# instead of trying to turn it back into a local dataframe?
dog_list = []
dogs = db.dogs.find()
for dog in dogs:
    dog_list.append(dog)

dog_df = pd.DataFrame(dog_list)