from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this server is running!"

@app.route("/sum")
def calculate_sum():
    args = request.args
    number1 = float(args.get("number1"))
    number2 = float(args.get("number2"))
    total_sum = number1 + number2
    return str(total_sum)

@app.route("/sum/<number1>/<number2>")
def calc_sum(number1, number2):
    total_sum = float(number1) + float(number2)
    return str(total_sum)

if __name__ == '__main__':
    app.run(use_reloader = True, host='127.0.0.1', port=5000)


