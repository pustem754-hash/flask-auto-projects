from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        calc_type = data.get('type')
        
        if calc_type == 'percentage_of':
            number = float(data.get('number', 0))
            percentage = float(data.get('percentage', 0))
            result = (number * percentage) / 100
            formula = f'{percentage}% от {number} = {result}'
            
        elif calc_type == 'what_percentage':
            part = float(data.get('part', 0))
            whole = float(data.get('whole', 0))
            if whole == 0:
                return jsonify({'error': 'Деление на ноль невозможно'}), 400
            result = (part / whole) * 100
            formula = f'{part} составляет {result:.2f}% от {whole}'
            
        elif calc_type == 'increase':
            number = float(data.get('number', 0))
            percentage = float(data.get('percentage', 0))
            increase = (number * percentage) / 100
            result = number + increase
            formula = f'{number} + {percentage}% = {result}'
            
        elif calc_type == 'decrease':
            number = float(data.get('number', 0))
            percentage = float(data.get('percentage', 0))
            decrease = (number * percentage) / 100
            result = number - decrease
            formula = f'{number} - {percentage}% = {result}'
            
        else:
            return jsonify({'error': 'Неизвестный тип расчета'}), 400
            
        return jsonify({
            'result': round(result, 2),
            'formula': formula
        })
        
    except ValueError:
        return jsonify({'error': 'Некорректные данные'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5017)
