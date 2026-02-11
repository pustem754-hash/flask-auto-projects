from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Landing Page</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial; }
        .hero { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 100px 20px; text-align: center; }
        .hero h1 { font-size: 48px; margin-bottom: 20px; }
        .hero p { font-size: 20px; margin-bottom: 30px; }
        .btn { background: white; color: #667eea; padding: 15px 40px; border: none; border-radius: 30px; font-size: 18px; cursor: pointer; }
        .features { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; padding: 80px 20px; max-width: 1200px; margin: 0 auto; }
        .feature { text-align: center; padding: 30px; }
        .feature-icon { width: 80px; height: 80px; background: #667eea; border-radius: 50%; margin: 0 auto 20px; }
    </style>
</head>
<body>
    <div class="hero">
        <h1>landing для кофейни</h1>
        <p>Лучшее решение для вашего бизнеса</p>
        <button class="btn">Начать сейчас</button>
    </div>
    <div class="features">
        <div class="feature"><div class="feature-icon"></div><h3>Быстро</h3><p>Моментальный результат</p></div>
        <div class="feature"><div class="feature-icon"></div><h3>Надежно</h3><p>100% гарантия качества</p></div>
        <div class="feature"><div class="feature-icon"></div><h3>Просто</h3><p>Легко начать работу</p></div>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011)
