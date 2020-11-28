import requests
import pandas as pd 

# Get API data
r = requests.get("https://api.thedogapi.com/v1/breeds")
# print(r.status_code)

data = r.json()
# df1 = pd.DataFrame(data)
# print(df1.head())
# print(data[1])

data = data[1]

# print(next(iter(data.items())))

print(data["weight"]["imperial"])
