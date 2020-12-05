import requests
import pandas as pd 
import json
from flask import jsonify

# dog_size = ['medium']
# adj_list = ['dutiful']


def best_breed(adj_list, dog_size):

    # Get API data
    r = requests.get("https://api.thedogapi.com/v1/breeds")

    data = r.json()
    df1 = pd.DataFrame(data)
    df2 = df1[["name","temperament", "weight"]]

    # Explode out list of temperament adj
    df3 = df2.assign(temperament=df2.temperament.str.split(',')).explode('temperament')

    # Clean Data
    df3["temperament"] = df3["temperament"].str.lower()
    df3["temperament"] = df3["temperament"].str.strip()

    # turn df into a dict 
    dict_ = df3.to_dict('records')

    for i in dict_:
        i["weight"] = i["weight"]["imperial"]
        i["points"] = 0
        i['avg_weight'] = 0
        i['size_category'] = ''


    for i in dict_:
        if i["weight"] == 'up - 18':
            i["weight"] = '18 - 18'
        else:
            i["weight"] == i["weight"]

    # get avg weights
    for i in dict_:
        if len(i["weight"]) == 5:
            i['avg_weight'] = (int(i["weight"][4]) + int(i["weight"][0])) / 2
        elif len(i["weight"]) == 6:
            x =int(i["weight"][4] + i["weight"][5])
            i['avg_weight'] = (x + int(i["weight"][0])) / 2
        elif len(i["weight"]) == 7:
            x =int(i["weight"][5] + i["weight"][6])
            y =int(i["weight"][0] + i["weight"][1])
            i['avg_weight'] = (x + y) / 2
        elif len(i["weight"]) == 8:
            x =int(i["weight"][5] + i["weight"][6] + i["weight"][7])
            y =int(i["weight"][0] + i["weight"][1])
            i['avg_weight'] = (x + y) / 2
        elif len(i["weight"]) == 9:
            x =int(i["weight"][6] + i["weight"][7] + i["weight"][8])
            y =int(i["weight"][0] + i["weight"][1] + i["weight"][2])
            i['avg_weight'] = (x + y) / 2


    # categorize dog size based on avg weight
    for i in dict_:
        if i["avg_weight"] < 20:
            i["size_category"] = 'small'
        elif i["avg_weight"] < 60:
            i["size_category"] = 'medium'
        else:
            i["size_category"] = 'large'




    for c in adj_list:
        for i in dict_:
            for e in i:
                for t in e:
                    if c == [i][0]["temperament"]:
                        [i][0]["points"] += 1


    df4 = pd.DataFrame(dict_)

    df4 = df4[df4["size_category"] == dog_size[0]]

    df4 = df4[["name", "points"]]

    df5 = df4.groupby(by = ['name']).sum()

    df6 = df5.sort_values("points", ascending = False)
    df6 = df6.reset_index()
    df6 = df6.head()

    dict7 = df6.to_dict()

    # final = json.dumps(dict7)

    # print(dict7)
    return dict7

# best_breed(adj_list, dog_size)