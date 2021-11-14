import requests

url = "https://jsonplaceholder.typicode.com/todos/10"

res = requests.delete(url)

print(res.json())
print(res)
