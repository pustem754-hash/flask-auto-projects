from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('index.html', title='Добро пожаловать!', message='Это простое Flask приложение')

@app.route('/about')
def about():
 return render_template('index.html', title='О проекте', message='Создано с помощью OpenClaw AI')

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0', port=5003)