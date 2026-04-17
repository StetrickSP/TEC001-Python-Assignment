from flask import Flask, request
import json


app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running!"

@app.route("/weather/<city_name>")
def get_weather_endpoint(city_name):
    cities = {
        "HCM": {
            "temp": 35,
            "conditions": "Cloudy",
            "forecast": [36,37,34]
        },
        "HN": {
            "temp": 32,
            "conditions": "Cloudy",
            "forecast": [36,37,34]
        },
        "TH": {
            "temp": 30,
            "conditions": "Cloudy",
            "forecast": [40,25,30]
        }
    }
    return json.dumps(cities[city_name])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)



