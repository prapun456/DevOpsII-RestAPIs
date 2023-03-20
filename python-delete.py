import requests
api_url = 'http://jsonplaceholder.typicode.com/todos/1'
response = requests.delete(api_url)
print(response.json())
print(response.status_code)
