from flask import Flask, request, jsonify
from Class import Calculator
app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    expr = request.json['expression']
    result = Calculator().calc_string(expr)
    return (jsonify({'answer':result}), 200)


if __name__ == '__main__':
    app.run(debug = True)