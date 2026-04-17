from flask import Flask, request

import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, the server is running!"

@app.route("/convert/<amount>/<from_currency>/<to_currency>") ## when getting data from api, queries will return type string, so remember to convert first
def convert_currency_api(amount, from_currency, to_currency):
    rates = {
        'USD': 1.0,
        'EUR': 0.9,
        'GBP': 0.7
    }

    if from_currency in rates and to_currency in rates: 
        result = float(amount) * rates[from_currency] * rates[to_currency]
        return json.dumps({
        "status": "success",
        "converted_amount": result
        })
    else:
        return json.dumps({
            "status": "fail",
            "error": "unsupported currency"
        })

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)




