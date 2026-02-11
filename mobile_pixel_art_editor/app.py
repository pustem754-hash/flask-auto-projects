from flask import Flask, render_template, request, jsonify, send_file
import json
import io
from PIL import Image, ImageDraw
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_image', methods=['POST'])
def save_image():
    data = request.json
    grid = data['grid']
    
    # Создаем изображение 320x320 (16x16 пикселей по 20px каждый)
    img = Image.new('RGB', (320, 320), 'white')
    draw = ImageDraw.Draw(img)
    
    # Рисуем пиксели
    for row in range(16):
        for col in range(16):
            color = grid[row][col]
            if color != '#FFFFFF':  # Не рисуем белые пиксели
                x1 = col * 20
                y1 = row * 20
                x2 = x1 + 20
                y2 = y1 + 20
                draw.rectangle([x1, y1, x2, y2], fill=color)
    
    # Сохраняем в память
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='pixel_art.png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5008)