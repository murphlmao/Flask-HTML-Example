import requests

s = requests.Session()

r = s.get('http://localhost:5000/test')
print(r.status_code)
print(r.content.decode())