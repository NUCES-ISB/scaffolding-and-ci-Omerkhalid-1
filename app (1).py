from flask import Flask, jsonify, render_template



app = Flask(__name__)

def add(x, y):
    return x + y


def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y  

def mod(x, y):
    return x % y


@app.route('/calc/add/<int:x>/<int:y>', methods=['GET'])
def addition(x, y):
    result = add(x, y)
    return jsonify({'result': result})


@app.route('/calc/multiply/<int:x>/<int:y>', methods=['GET'])
def multiplication(x, y):
    result = multiply(x, y)
    return jsonify({'result': result})

# Route for division
@app.route('/calc/divide/<int:x>/<int:y>', methods=['GET'])
def division(x, y):
    # Check for division by zero
    if y == 0:
        return jsonify({'error': 'Division by zero is not allowed'}), 400
    result = divide(x, y)
    return jsonify({'result': result})

# Route for modulus
@app.route('/calc/mod/<int:x>/<int:y>', methods=['GET'])
def modulus(x, y):
    # Check for division by zero
    if y == 0:
        return jsonify({'error': 'Division by zero is not allowed'}), 400
    result = mod(x, y)
    return jsonify({'result': result})

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)