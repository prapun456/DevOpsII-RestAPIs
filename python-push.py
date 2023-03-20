import requests
api_url = 'http://jsonplaceholder.typicode.com/todos'
response = requests.get(api_url)
print(response.json())

todo ={
    "UserId" : 1,
    "id" : 1,
    "title" : 'Putcharapon Kaewmahanil',
    "completed" : True
}
response = requests.put(api_url, json=todo)



print(response.json())
print(response.status_code)