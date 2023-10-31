import requests

content = requests.post('http://127.0.0.1:8000/auth/login', data ={"username": "admin2", "password": "admin2"})
print(content.json())