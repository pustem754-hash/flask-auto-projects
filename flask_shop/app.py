from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    products = [
        {"name": "Ноутбук", "price": 85000},
        {"name": "iPhone", "price": 120000},
        {"name": "Наушники", "price": 15000}
    ]
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
