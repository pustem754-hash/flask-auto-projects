from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
    <head>
        <meta charset="utf-8">
        <title>ЖКХ Приложение</title>
        <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background: white;
            padding: 60px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
        }
        h1 {
            color: #667eea;
            font-size: 3em;
            margin-bottom: 20px;
        }
        p {
            color: #666;
            font-size: 1.3em;
            margin: 10px 0;
        }
        .emoji {
            font-size: 4em;
            margin-bottom: 20px;
        }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">🏠</div>
            <h1>ЖКХ Приложение</h1>
            <p>✅ Приложение работает!</p>
            <p>🔌 Порт: 5010</p>
            <p>⏰ Создано: 2026-02-10 21:41:57</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010)
