import requests

url = "https://jsonplaceholder.typicode.com/todos/10"

data = {"title": "Wash car"}

res = requests.patch(url, json = data)
print("patch")
print(res.json())
print(res)

#res = requests.put(url, json = data)
#print("put")
#print(res.json())
#print(res)
