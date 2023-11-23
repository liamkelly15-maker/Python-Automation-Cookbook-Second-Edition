import requests

result=requests.get('https://jsonplaceholder.typicode.com/posts')
print(result.json())