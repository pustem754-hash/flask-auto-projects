from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return """<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Создай landing для ресторана итальянской кухни</title><style>*{margin:0;padding:0}body{font-family:Arial}.hero{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:2rem}h1{font-size:4rem}.cta{background:#fff;color:#667eea;padding:1.5rem 3rem;border:none;border-radius:50px;font-size:1.5rem;margin-top:2rem}</style></head><body><div class="hero"><div><h1>Создай landing для ресторана итальянской кухни</h1><p style="font-size:1.5rem;margin-top:1rem">Лучшее решение</p><button class="cta">Узнать больше</button></div></div></body></html>"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5016)