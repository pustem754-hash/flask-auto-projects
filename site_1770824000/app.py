
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return """
<h1>САЙТ О МОНТАЖЕ ТРУБ</h1><p>Сайт создан через OpenClaw Bot</p>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=False)
