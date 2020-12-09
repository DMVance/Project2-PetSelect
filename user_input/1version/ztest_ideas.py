import requests
import pandas as pd 
import json

# Get API data
r = requests.get("https://api.thedogapi.com/v1/breeds")
# print(r.status_code)

data = r.json()
# data = json.dumps(data)
# print(data)
# print(data[:])
# print(type(data))
# print(type(data[0]))
# data = data[1]

# data2 = data.read_json(_, orient='records')
# print(data2)

# data_file = open("data")
# print(data_file)
# data_str = data_file.read()
# data_data = json.loads(data_str)[0]
# print(data_data)

# for d in data:
#     for k, v in d.items():
#         print(k, v)

# dog_dict = {}
# for d in data:
#     key = list(d.keys())[0]
#     val = d[key]
#     dog_dict[key] = val
# print(dog_dict)

# data2 = json.loads(data)[0]
# print(data2)

# data2 = dict(d.popitem() for d in data)
# print(json.dumps(data2, indent=4))  # Pretty-print result.


# dog_dict = {}
# for d in data:
#     key = list(d.keys())[0]
#     val = d[key]
#     data[key] = val
# print(dog_dict)


# data = r.text[1:-1]

# # print(data)


# dog_dict = {}
# for d in data:
#     key = list(d.keys())
#     val = d[key]
#     dog_dict[key] = val
# print(dog_dict)













# print(data["weight"]["imperial"])

# data2 = data["weight"]["imperial"]
# print(data2)


# del data["height"]
# del data["country_code"]
# del data["bred_for"]
# del data["breed_group"]
# del data["life_span"]
# del data["origin"]


# for d in data: 
#     for i in d:
#         d["weight"] = d["weight"]["imperial"]
#         d["points"] = 0

# data["weight"] = data["weight"]["imperial"]
# data["points"] = 0

# for k, v in data.items():
#     print(k, v)

df = pd.DataFrame(data, index = [0])
print(df)

# df1 = pd.DataFrame(data, index = [0])
# print(df1.head())

# # Explode out list of temperament adj
# df3 = df2.assign(temperament=df2.temperament.str.split(',')).explode('temperament')
# df3 = df3.reset_index()
# df3 = df3.set_index("id")

# # Clean Data
# df3["temperament"] = df3["temperament"].str.lower()
# df3["temperament"] = df3["temperament"].str.strip()
# print(df3.head()) 

# # turn df into a dict 

# # dict_ = df3.to_dict('records')
# # print(dict_)
# # print(dict_[49]['temperament'])
