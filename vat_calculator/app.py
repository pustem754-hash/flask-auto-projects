from flask import Flask, render_template, request, jsonify
from decimal import Decimal, ROUND_HALF_UP

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_vat():
    try:
        data = request.get_json()
        amount = Decimal(str(data['amount']))
        vat_rate = Decimal(str(data['vat_rate']))
        calculation_type = data['calculation_type']
        
        if calculation_type == 'add':
            # Добавить НДС к сумме
            vat_amount = (amount * vat_rate / 100).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            total_amount = amount + vat_amount
            base_amount = amount
        else:
            # Выделить НДС из суммы
            base_amount = (amount / (1 + vat_rate / 100)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            vat_amount = amount - base_amount
            total_amount = amount
        
        return jsonify({
            'success': True,
            'base_amount': float(base_amount),
            'vat_amount': float(vat_amount),
            'total_amount': float(total_amount),
            'vat_rate': float(vat_rate)
        })
    
    except (ValueError, KeyError) as e:
        return jsonify({
            'success': False,
            'error': 'Некорректные данные'
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5009)