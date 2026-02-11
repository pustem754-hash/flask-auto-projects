import os
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML = '''<!DOCTYPE html>
<html>
<head><title>Flask Calculator</title>
<style>
body { font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; }
input, button { padding: 10px; margin: 5px; font-size: 16px; }
button { background: #007bff; color: white; border: none; cursor: pointer; }
#result { margin-top: 20px; padding: 15px; background: #f0f0f0; }
</style></head>
<body>
<h1>Calculator</h1>
<input type="number" id="num1" placeholder="Number 1">
<input type="number" id="num2" placeholder="Number 2"><br>
<button onclick="calc('add')">+</button>
<button onclick="calc('subtract')">-</button>
<button onclick="calc('multiply')">×</button>
<button onclick="calc('divide')">÷</button>
<div id="result"></div>
<script>
async function calc(op) {
    const n1 = parseFloat(document.getElementById('num1').value);
    const n2 = parseFloat(document.getElementById('num2').value);
    const res = await fetch('/' + op, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({num1: n1, num2: n2})});
    const data = await res.json();
    document.getElementById('result').innerText = data.error ? 'Error: ' + data.error : 'Result: ' + data.result;
}
</script>
</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    return jsonify({'result': data['num1'] + data['num2']})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.json
    return jsonify({'result': data['num1'] - data['num2']})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    return jsonify({'result': data['num1'] * data['num2']})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.json
    if data['num2'] == 0:
        return jsonify({'error': 'Cannot divide by zero'}), 400
    return jsonify({'result': data['num1'] / data['num2']})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5010))
    app.run(host='0.0.0.0', port=port, debug=True)
