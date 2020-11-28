import requests

r = requests.get("https://api.thedogapi.com/v1/breeds")

data = r.json()
print(json.dumps(data))