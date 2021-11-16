import requests

url = 'http://localhost:5001/api'
r = requests.post(url,json={'exp':1.8,})
print(r.json())

url = 'http://localhost:5001/inference'
r = requests.post(url,json={'exp':1.8,})
print(r.json())

url = 'http://localhost:5001/user_info'
r = requests.post(url,json={'user_id':'13'})
print(r.json())
