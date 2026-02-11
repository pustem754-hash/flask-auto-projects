from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Портфолио</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial; margin: 0; padding: 20px; background: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 { color: #333; text-align: center; }
        .gallery { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 40px; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .card img { width: 100%; height: 200px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 4px; }
        .card h3 { margin: 15px 0 10px; }
        .card p { color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Портфолио - Создай портфолио дизайнера</h1>
        <div class="gallery">
            <div class="card"><div style="width:100%;height:200px;background:linear-gradient(135deg,#667eea,#764ba2);border-radius:4px;"></div><h3>Проект 1</h3><p>Описание проекта</p></div>
            <div class="card"><div style="width:100%;height:200px;background:linear-gradient(135deg,#f093fb,#f5576c);border-radius:4px;"></div><h3>Проект 2</h3><p>Описание проекта</p></div>
            <div class="card"><div style="width:100%;height:200px;background:linear-gradient(135deg,#4facfe,#00f2fe);border-radius:4px;"></div><h3>Проект 3</h3><p>Описание проекта</p></div>
            <div class="card"><div style="width:100%;height:200px;background:linear-gradient(135deg,#43e97b,#38f9d7);border-radius:4px;"></div><h3>Проект 4</h3><p>Описание проекта</p></div>
            <div class="card"><div style="width:100%;height:200px;background:linear-gradient(135deg,#fa709a,#fee140);border-radius:4px;"></div><h3>Проект 5</h3><p>Описание проекта</p></div>
            <div class="card"><div style="width:100%;height:200px;background:linear-gradient(135deg,#30cfd0,#330867);border-radius:4px;"></div><h3>Проект 6</h3><p>Описание проекта</p></div>
        </div>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5014)
