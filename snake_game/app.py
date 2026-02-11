
import os
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Snake Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        #game-container {
            width: 400px;
            height: 400px;
            border: 1px solid black;
            position: relative;
        }
        #score {
            position: absolute;
            top: 10px;
            left: 10px;
            font-size: 24px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id='game-container'>
        <div id='score'>Score: <span id='score-value'>0</span></div>
        <canvas id='game-canvas' width='400' height='400'></canvas>
    </div>
    <script>
        let score = 0;
        let snake = [{x: 200, y: 200}, {x: 190, y: 200}, {x: 180, y: 200}];
        let direction = 'right';
        let food = {x: Math.floor(Math.random() * 40) * 10, y: Math.floor(Math.random() * 40) * 10};
        let canvas = document.getElementById('game-canvas');
        let ctx = canvas.getContext('2d');
        let scoreElement = document.getElementById('score-value');

        function draw() {
            ctx.clearRect(0, 0, 400, 400);
            for (let i = 0; i < snake.length; i++) {
                ctx.fillStyle = 'green';
                ctx.fillRect(snake[i].x, snake[i].y, 10, 10);
            }
            ctx.fillStyle = 'red';
            ctx.fillRect(food.x, food.y, 10, 10);
            scoreElement.textContent = score;
        }

        function update() {
            let head = snake[0];
            if (direction === 'right') {
                head = {x: head.x + 10, y: head.y};
            } else if (direction === 'left') {
                head = {x: head.x - 10, y: head.y};
            } else if (direction === 'up') {
                head = {x: head.x, y: head.y - 10};
            } else if (direction === 'down') {
                head = {x: head.x, y: head.y + 10};
            }
            snake.unshift(head);
            if (snake[0].x === food.x && snake[0].y === food.y) {
                score++;
                food = {x: Math.floor(Math.random() * 40) * 10, y: Math.floor(Math.random() * 40) * 10};
            } else {
                snake.pop();
            }
            if (snake[0].x < 0 || snake[0].x >= 400 || snake[0].y < 0 || snake[0].y >= 400 || checkCollision()) {
                alert('Game Over!');
                location.reload();
            }
        }

        function checkCollision() {
            for (let i = 1; i < snake.length; i++) {
                if (snake[0].x === snake[i].x && snake[0].y === snake[i].y) {
                    return true;
                }
            }
            return false;
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' && direction !== 'left') {
                direction = 'right';
            } else if (e.key === 'ArrowLeft' && direction !== 'right') {
                direction = 'left';
            } else if (e.key === 'ArrowUp' && direction !== 'down') {
                direction = 'up';
            } else if (e.key === 'ArrowDown' && direction !== 'up') {
                direction = 'down';
            }
        });

        setInterval(() => {
            update();
            draw();
        }, 100);
    </script>
</body>
</html>
'''
      app.route('/')(lambda: render_template_string(html))
      app.route('/get_score', methods=['GET'])(lambda: jsonify({'score': score}))
      if __name__ == '__main__':
          app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    