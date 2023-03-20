import requests
api_url = 'http://jsonplaceholder.typicode.com/todos'

todo ={
    "UserId" : 909,
    "id" : 909,
    "title" : 'Putcharapon Kaewmahanil',
    "completed" : False
}
response = requests.post(api_url, json=todo)



print(response.json())
print(response.status_code)