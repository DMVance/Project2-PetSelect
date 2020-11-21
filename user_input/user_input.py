import requests
import pandas as pd 

# Get API data
r = requests.get("https://api.thedogapi.com/v1/breeds")
# print(r.status_code)

data = r.json()
df1 = pd.DataFrame(data)
# print(df)
df2 = df1[["id","name","temperament"]]
df2["points"] = 0
# print(adj)

# Explode out list of temperament adj
df3 = df2.assign(temperament=df2.temperament.str.split(',')).explode('temperament')
df3 = df3.reset_index()
# df3 = df3.set_index("temperament")
# df3 = df3["temperament"].lower()
# print(df3.head()) 

# turn df into a dict 

dict_ = df3.to_dict('records')
# print(dict_)
# print(dict_[49]['temperament'])



# for i in dict_:
#     print([i][0]["temperament"])


# Create input for user
## add data validation so they can only choose items in the list

adj_list = [] 

def main():
    while True:
        print("-" * 50)
        print("Let's Find Your Perfect Pup!")

        user_choice = input("What characteristics would you like in your dog? Type out adjectives. Press q when you're done.\n")
        
        if user_choice == "q":
            break

        adj_list.append(user_choice)

        print(adj_list)
        
        # Take user input and match it to the adj list of temperaments
        # for t in df3["temperament"]:
        #     if [df3[df3["temperament"] == user_choice]]:
        #         df3["points"] += 1

        # t_index = []

        # for t in df3["temperament"]:
        #     if [df3[df3["temperament"] == user_choice]]:
        #         t_index.append([df3[df3["temperament"].index.values]])
                # df3["points"].index.values += 1
        
        ##I think instead of making the temperaments a data frame, I should make them a dictionary and add the count that way. 





main()

# print(f"You want a dog that is {adj_list}")

for c in adj_list:
    for i in dict_:
        for e in i:
            for t in e:
                if c == [i][0]["temperament"]:
                    [i][0]["points"] += 1

for a in adj_list:
    print(f"You want a dog that is {a}")

# print(df3)
# print(t_index)
    
print(dict_)

