
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Создай портфолио фотографа</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #f4f4f4; }
        .hero { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 4rem 2rem; text-align: center; }
        .portfolio { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; padding: 2rem; max-width: 1200px; margin: 0 auto; }
        .item { background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { font-size: 3rem; margin-bottom: 1rem; }
    </style>
</head>
<body>
    <div class="hero">
        <h1>Создай портфолио фотографа</h1>
        <p>Мои работы и проекты</p>
    </div>
    <div class="portfolio">
        <div class="item"><h3>Проект 1</h3><p>Описание проекта</p></div>
        <div class="item"><h3>Проект 2</h3><p>Описание проекта</p></div>
        <div class="item"><h3>Проект 3</h3><p>Описание проекта</p></div>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5015)
