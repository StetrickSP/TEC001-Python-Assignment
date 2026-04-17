import requests

req = "http://127.0.0.1:5000/convert/5/USD/ER"

res = requests.get(req).json()

print(res)