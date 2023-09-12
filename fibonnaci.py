from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to calculate the Fibonacci number at index n
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    try:
        n = int(request.args.get('number'))
        if n < 0:
            return jsonify({'error': 'Index must be non-negative'}), 400

        result = fibonacci(n)
        return jsonify({'index': n, 'fibonacci_value': result})
    except ValueError:
        return jsonify({'error': 'Invalid input, please provide a valid integer'}), 400

if __name__ == '__main__':
    app.run(debug=True)