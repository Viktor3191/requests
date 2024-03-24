import requests

website = 'https://jsonplaceholder.typicode.com/posts/10'
print(requests.get(website).json())

response = requests.put(website, data={
    'id': 10,
    "userId": 100,
    "title": "my first post100",
    "body": 'body for my post100'
})
print(response.json())