import requests

# req = "http://127.0.0.1:5000/sum?number1=10&number2=20"
req1 = "http://127.0.0.1:5002/weather/HCM"

# res = requests.get(req).json()
res1 = requests.get(req1).json()

print(res1)