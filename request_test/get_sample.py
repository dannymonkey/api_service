import requests

url = "https://jsonplaceholder.typicode.com/todos/10"

res = requests.get(url)

print(res.content)
print(res.json())
print(res)
