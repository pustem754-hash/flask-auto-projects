from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
    <head>
        <meta charset="utf-8">
        <title>Базовое приложение</title>
        <style>
        body {
            font-family: Arial;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .box {
            background: white;
            padding: 60px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
        }
        h1 {
            color: #667eea;
            font-size: 3em;
            margin: 0 0 20px 0;
        }
        p {
            color: #666;
            font-size: 1.3em;
        }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Базовое приложение</h1>
            <p>Приложение работает!</p>
            <p>Порт: 5016</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5016)
