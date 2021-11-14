import requests

url = "https://jsonplaceholder.typicode.com/todos/"

data = {"userId": 1, "title": "Buy milk", "completed": False}

res = requests.post(url, json = data)

print(res, res.content)
