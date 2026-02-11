from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        original_price = float(data.get('original_price', 0))
        discount_percent = float(data.get('discount_percent', 0))
        
        # Расчёт
        discount_amount = original_price * (discount_percent / 100)
        final_price = original_price - discount_amount
        savings = discount_amount
        
        result = {
            'original_price': round(original_price, 2),
            'discount_percent': discount_percent,
            'discount_amount': round(discount_amount, 2),
            'final_price': round(final_price, 2),
            'savings': round(savings, 2)
        }
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5015, debug=True)
