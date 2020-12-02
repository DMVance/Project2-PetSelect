import requests
import pandas as pd 

# Get API data
r = requests.get("https://api.thedogapi.com/v1/breeds")

data = r.json()
df1 = pd.DataFrame(data)
df2 = df1[["name","temperament", "weight"]]

# Explode out list of temperament adj
df3 = df2.assign(temperament=df2.temperament.str.split(',')).explode('temperament')
# df3 = df3.reset_index()
# df3 = df3.set_index("temperament")

# Clean Data
df3["temperament"] = df3["temperament"].str.lower()
df3["temperament"] = df3["temperament"].str.strip()

# print(df3.head()) 

# turn df into a dict 
dict_ = df3.to_dict('records')
# print(dict_)
# print(dict_[49]['temperament'])

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

# for i in dict_:
#     for w in i["weight"]:
#         if w == 'up - 18':
#             w = '18 - 18'
#         else:
#             w == w


# check data for weight
# weight_list = []
# for i in dict_: 
#     if i["weight"] not in weight_list:
#         weight_list.append(i["weight"])
# print(weight_list)
# for i in weight_list:
#     if len(i) == 7:
#         print(i)


# get avg weights
for i in dict_:
    # data cleaning
    # if i["weight"] == 'up - 18':
    #     i['avg_weight'] = 18
    #calculate avg weights by len of weights given
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



# Small Dog# 0-20 pounds
# Medium Dog# 21-60 pounds
# Large Dog# 61+ pounds

# categorize dog size based on avg weight
for i in dict_:
    if i["avg_weight"] < 20:
        i["size_category"] = 'small'
    elif i["avg_weight"] < 60:
        i["size_category"] = 'medium'
    else:
        i["size_category"] = 'large'


# for i in dict_:
#     print([i])


# get list of adj for the different dog sizes

# large
large_adj = []
for i in dict_: 
    if i["size_category"] == 'large' and i["temperament"] not in large_adj:
        large_adj.append(i["temperament"])
# print(large_adj)

# medium
medium_adj = []
for i in dict_: 
    if i["size_category"] == 'medium' and i["temperament"] not in medium_adj:
        medium_adj.append(i["temperament"])
# print(medium_adj)

# small
small_adj = []
for i in dict_: 
    if i["size_category"] == 'small' and i["temperament"] not in small_adj:
        small_adj.append(i["temperament"])
# print(small_adj)

def size_(user_size):
    if user_size == "small":
        return small_adj
    elif user_size == 'medium':
        return medium_adj
    else:
        return large_adj
        