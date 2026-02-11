from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>/root/openclaw_dashboard.sh</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 50px 0;
        }
        .hero {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 80px 0;
            text-align: center;
            border-radius: 20px;
            margin-bottom: 50px;
        }
        .card {
            border: none;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s;
            margin-bottom: 30px;
        }
        .card:hover {
            transform: translateY(-10px);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="hero">
            <h1 class="display-3 fw-bold mb-4">🚀 /root/openclaw_dashboard.sh</h1>
            <p class="lead">Создано OPENCLAW BOT</p>
        </div>
        <div class="row g-4">
            <div class="col-md-4">
                <div class="card p-4 text-center">
                    <i class="fas fa-magic fa-3x text-primary mb-3"></i>
                    <h3>Инновации</h3>
                    <p class="text-muted">Современные технологии</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card p-4 text-center">
                    <i class="fas fa-rocket fa-3x text-success mb-3"></i>
                    <h3>Скорость</h3>
                    <p class="text-muted">Быстрая разработка</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card p-4 text-center">
                    <i class="fas fa-shield-alt fa-3x text-danger mb-3"></i>
                    <h3>Безопасность</h3>
                    <p class="text-muted">Защита данных</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011)
