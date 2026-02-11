from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return """<!DOCTYPE html><html><head><meta charset="UTF-8"><title>создай презентацию маркетолога</title><style>*{margin:0;padding:0}body{font-family:Arial}header{background:#2c3e50;color:#fff;padding:2rem;text-align:center}.container{max-width:1200px;margin:0 auto;padding:3rem 2rem}h1{font-size:2.5rem}</style></head><body><header><h1>создай презентацию маркетолога</h1></header><div class="container"><h2>Добро пожаловать!</h2></div></body></html>"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5017)