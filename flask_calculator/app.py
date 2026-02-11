
import os
from flask import Flask, render_template_string

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Flask Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-image: linear-gradient(to bottom right, #4567b7, #6495ed);
            background-size: 100% 100%;
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .calculator {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }
        .display {
            width: 200px;
            height: 40px;
            background-color: #fff;
            border: none;
            border-radius: 10px;
            padding: 10px;
            font-size: 20px;
            text-align: right;
        }
        .button {
            width: 50px;
            height: 50px;
            background-color: #fff;
            border: none;
            border-radius: 10px;
            margin: 5px;
            font-size: 20px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #ccc;
        }
    </style>
</head>
<body>
    <div class='calculator'>
        <input type='text' id='display' class='display' disabled>
        <div>
            <button class='button' onclick='calculate("+")'>+</button>
            <button class='button' onclick='calculate("-")'>-</button>
            <button class='button' onclick='calculate("*")'>*</button>
            <button class='button' onclick='calculate("/")'>/</button>
        </div>
        <div>
            <button class='button' onclick='calculate("7")'>7</button>
            <button class='button' onclick='calculate("8")'>8</button>
            <button class='button' onclick='calculate("9")'>9</button>
            <button class='button' onclick='clearDisplay()'>C</button>
        </div>
        <div>
            <button class='button' onclick='calculate("4")'>4</button>
            <button class='button' onclick='calculate("5")'>5</button>
            <button class='button' onclick='calculate("6")'>6</button>
            <button class='button' onclick='calculate("=")'>=</button>
        </div>
        <div>
            <button class='button' onclick='calculate("1")'>1</button>
            <button class='button' onclick='calculate("2")'>2</button>
            <button class='button' onclick='calculate("3")'>3</button>
            <button class='button' onclick='calculate("0")'>0</button>
        </div>
    </div>
    <script>
        let display = document.getElementById('display');
        let expression = '';
        function calculate(value) {
            if (value === '=') {
                try {
                    let result = eval(expression);
                    display.value = result;
                    expression = result.toString();
                } catch (e) {
                    display.value = 'Error';
                    expression = '';
                }
            } else if (value === 'C') {
                display.value = '';
                expression = '';
            } else {
                expression += value;
                display.value = expression;
            }
        }
        function clearDisplay() {
            display.value = '';
            expression = '';
        }
    </script>
</body>
</html>
'''
      @app.route('/')
      def index():
          return render_template_string(html)

      if __name__ == '__main__':
          app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
      