import requests

url = "https://jsonplaceholder.typicode.com/todos/10"

res = requests.get(url)
print(res.json())

data = {"userId": 1, "title": "Wash car", "completed": True}
res = requests.put(url, json = data)
print(res.json())
print(res)

