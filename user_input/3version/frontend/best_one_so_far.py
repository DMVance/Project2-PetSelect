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



# Create input for user
adj_list = [] 
dog_size = []

def size():
    ##need to add in protections so they can only enter small medium or large
    user_size = input("Do you want a small, medium, or large dog?\n")
    dog_size.append(user_size)
    # dog_size = dog_size[0]

    size_df = pd.DataFrame(dog_size)
    size_df.to_html("results/dog_size.html")

size()
# print(dog_size)

def choice():
    while True:
        print("-" * 50)
        print("Let's Find Your Perfect Pup!")

        print(f"These are adjectives that describe {dog_size[0]} dogs.\n")

        if dog_size[0] == "small":
            print(small_adj)
            small_adj_df = pd.DataFrame(small_adj)
            small_adj_df.to_html("results/adj_list.html")
        elif dog_size[0] == 'medium':
            print(medium_adj)
            medium_adj_df = pd.DataFrame(medium_adj)
            medium_adj_df.to_html("results/adj_list.html")
        else:
            print(large_adj)
            large_adj_df = pd.DataFrame(large_adj)
            large_adj_df.to_html("results/adj_list.html")

        user_choice = input("What characteristics would you like in your dog? Type out adjectives. Press q when you're done.\n")
        
        if user_choice == "q":
            break

        adj_list.append(user_choice)

        print(adj_list)

        adj_df = pd.DataFrame(adj_list)
        adj_df.to_html("results/user_adj_list.html")


choice()

# print(f"You want a dog that is {adj_list}")

# this fucking works kind of! keeping it as a reference
# for c in adj_list:
#     for i in dict_:
#         for e in i:
#             for t in e:
#                 if c == [i][0]["temperament"]:
#                     [i][0]["points"] += 1

def best_breed():
    for c in adj_list:
        for i in dict_:
            for e in i:
                for t in e:
                    if c == [i][0]["temperament"]:
                        [i][0]["points"] += 1



    for a in adj_list:
        print(f"You want a dog that is {a}")

    # print(dict_)

    df4 = pd.DataFrame(dict_)
    # print(df4)

    # above_35 = titanic[titanic["Age"] > 35]
    df4 = df4[df4["size_category"] == dog_size[0]]
    # print(df4)

    # ages = titanic["Age"]
    df4 = df4[["name", "points"]]

    df5 = df4.groupby(by = ['name']).sum()
    # print(df5.head())

    df6 = df5.sort_values("points", ascending = False)
    df6 = df6.reset_index()
    print(df6.head())

    # df6.to_html("results/best_breed.html")

best_breed()


# the data that needs to be linked to the API would be color, age, sex, etc. data in the API
