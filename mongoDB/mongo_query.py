import os
import pymongo
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json

CONN = os.getenv("CONN")
client = pymongo.MongoClient(CONN)
db = client.austin_dogs

pd.options.display.max_columns = 999

# # FIND ALL
# all_dogs_list = []
# all_dogs_query = db.dogs.find()
# for dog in all_dogs_query:
#     all_dogs_list.append(dog)
# all_dogs_df = pd.DataFrame(all_dogs_list).drop(columns=['_id'])

# print("""
# ----------------------------------------
# All Dogs (Sample of first 20 results)
# ----------------------------------------
# """)
# print(all_dogs_df.head(20)


# FIND BREED
def find_breed(search_breed):
    breeds_query_dict = {
        "$or": [
            { 
                "primary_breed": {
                    "$regex": search_breed, 
                    "$options": "i"
                }
            },
            { 
                "secondary_breed": {
                    "$regex": search_breed, 
                    "$options": "i"
                }
            }
        ]
    }

    # ---print output for testing---
    breeds_query = db.dogs.find(breeds_query_dict)

    breeds_list = []
    for dog in breeds_query:
        breeds_list.append(dog)
    breeds_df = pd.DataFrame(breeds_list).drop(columns=['_id'])

    print("""
    ----------------------------------------
    Dog breed search (Sample of first 10 results)
    ----------------------------------------
    """)
    print(breeds_df.head(10))

    return breeds_query_dict


# FIND AGE
def find_age(youngest_yrs, youngest_mos, oldest_yrs, oldest_mos):
    # this portion calculates a range of birthdays based on user's desired age range
    youngest_bday = datetime.today() - relativedelta(years=youngest_yrs, months=youngest_mos)
    oldest_bday = datetime.today() - relativedelta(years=oldest_yrs, months=oldest_mos)
    # the dictionary below constructs an "and" query that
    # searches the birthday field for dates greater than or equal to
    # the youngest desired birthday and less than or equal to
    # the oldest desired birthday
    ages_query_dict = { 'birthday': { '$gte': oldest_bday, '$lt': youngest_bday } }
    
    # ---print output for testing---
    ages_query = db.dogs.find(ages_query_dict)

    ages_list = []
    for dog in ages_query:
        ages_list.append(dog)
    ages_df = pd.DataFrame(ages_list)

    print(f"Oldest dog desired birthday: {oldest_bday.month}/{oldest_bday.day}/{oldest_bday.year}")
    print(f"Youngest dog desired birthday: {youngest_bday.month}/{youngest_bday.day}/{youngest_bday.year}")

    print("""
    ----------------------------------------
    Dog age search (Sample of first 10 results)
    ----------------------------------------
    """)
    print(ages_df.head(10))

    return ages_query_dict


# FIND MALE/FEMALE
def find_sex(search_sex):
    sex_query_dict = {
        "sex": {
            "$regex": search_sex, 
            "$options": "i"
        }
    }

    # ---print output for testing---
    sex_query = db.dogs.find(sex_query_dict)

    sex_list = []
    for dog in sex_query:
        sex_list.append(dog)
    sex_df = pd.DataFrame(sex_list).drop(columns=['_id'])

    print("""
    ----------------------------------------
    Dog male/female search (Sample of first 10 results)
    ----------------------------------------
    """)
    print(sex_df.head(10))

    return sex_query_dict

# FIND COLOR
def find_color(search_color):
    colors_query_dict = {
        "$or": [
            { 
                "primary_color": {
                    "$regex": search_color, 
                    "$options": "i"
                }
            },
            { 
                "secondary_color": {
                    "$regex": search_color, 
                    "$options": "i"
                }
            }
        ]
    }

    # ---print output for testing---
    colors_query = db.dogs.find(colors_query_dict)

    colors_list = []
    for dog in colors_query:
        colors_list.append(dog)
    colors_df = pd.DataFrame(colors_list).drop(columns=['_id'])

    print("""
    ----------------------------------------
    Dog color search (Sample of first 10 results)
    ----------------------------------------
    """)
    print(colors_df.head(10))

    return colors_query_dict

# FIND CONDITION UPON INTAKE (E.G. SICK, INJURED)
def find_injured(search_injured):
    if search_injured:
        injured_query_dict = {
            "intake_condition": {
                "$not": {
                    "$regex": "Normal",
                    "$options": "i"
                }
            }
        }
    else:
        injured_query_dict = {
            "intake_condition": {
                "$regex": "Normal", 
                "$options": "i"
            }
        }


    # ---print output for testing---
    injured_query = db.dogs.find(injured_query_dict)

    injured_list = []
    for dog in injured_query:
        injured_list.append(dog)
    injured_df = pd.DataFrame(injured_list).drop(columns=['_id'])

    print("""
    ----------------------------------------
    Dog sick/injured search (Sample of first 10 results)
    ----------------------------------------
    """)
    print(injured_df.head(10))

    return injured_query_dict


# COMBINE QUERY CONDITIONS
def combined_queries(search_breed, youngest_yrs, youngest_mos, oldest_yrs, oldest_mos, search_sex, search_color, search_injured):
    list_of_query_dicts = [
        find_breed(search_breed), 
        find_age(youngest_yrs, youngest_mos, oldest_yrs, oldest_mos), 
        find_sex(search_sex),
        find_color(search_color),
        find_injured(search_injured),
    ]
    combined_queries_dict = { "$and": list_of_query_dicts }
    combined_query = db.dogs.find(combined_queries_dict)

    combined_dogs_list = []
    for dog in combined_query:
        combined_dogs_list.append(dog)
    combined_dogs_df = pd.DataFrame(combined_dogs_list)

    combined_dogs_df = combined_dogs_df.drop(columns=["_id"])

    # ---below this just for testing---
    print("""
    ----------------------------------------
    Combined query search (Sample of first 20 results)
    ----------------------------------------
    """)
    print(combined_dogs_df.head(20))

    return combined_dogs_df

# GET USER INPUT
# This input function is just to test the functions above
# in our app implementation, the frontend interface should pass
# the user input to the combined_search function
def user_input():
    print("""
        Find a dog of a specific breed!
        """)
    search_breed = input("Desired breed: ")

    print("""
        Find a dog in a specific age range!
        Will request youngest desired age in years and months
        Then requests oldest desired age in years and months
        """)
    youngest_yrs = int(input("Youngest age years: "))
    youngest_mos = int(input("Youngest age months: "))
    oldest_yrs = int(input("Oldest age years: "))
    oldest_mos = int(input("Oldest age months: "))

    print("""
        Find a dog of a specific sex!
        """)
    search_sex = input("Desired male or female: ")

    print("""
        Find a dog of a specific color!
        """)
    search_color = input("Desired color: ")

    print("""
        Are you searching for a sick or injured dog to foster?
        """)
    injured_input = input("Foster sick/injured dog? (y/n): ")

    if injured_input.lower()[0] == "y":
        search_injured = True
    else:
        search_injured = False

    return (
        search_breed, 
        youngest_yrs, 
        youngest_mos, 
        oldest_yrs, 
        oldest_mos, 
        search_sex, 
        search_color, 
        search_injured
    )


# ===============================
# Call the search functions above

# Combined queries
# remember that user_input() won't be used in the app
# the arguments for the combined_queries() function will be
# collected by the frontend and passed to combined_queries()
# the user_input() function here is just to test the script

# search_params = user_input()

# combined_queries(*search_params)

# dogs_df = combined_queries("German Shepherd", 0, 3, 8, 5, "female", "brown", False)

dogs_df = combined_queries("", 0, 0, 100, 0, "", "", False)

print(dogs_df["primary_color"].unique())
print(dogs_df["secondary_color"].unique())


# columns = ["name", "primary_breed", "secondary_breed", "primary_color", "secondary_color", "age_years", "age_months", "age_days", "intake_condition"]

# dogs_df = dogs_df[columns]

# dogs_dicts = dogs_df.to_dict("records")

# dogs_json = json.dumps(dogs_dicts)

# print(type(dogs_json))
# print(dogs_json)