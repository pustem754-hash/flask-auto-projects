#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🐍 Змейка</title>
    <style>
        * {margin:0;padding:0;box-sizing:border-box}
        body {
            font-family:Arial;
            background:linear-gradient(135deg,#667eea,#764ba2);
            min-height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            padding:20px
        }
        .game {
            background:#fff;
            padding:30px;
            border-radius:20px;
            text-align:center;
            box-shadow:0 20px 60px rgba(0,0,0,0.3)
        }
        h1 {color:#667eea;margin-bottom:20px}
        .score {font-size:24px;color:#495057;margin:10px 0}
        canvas {
            border:3px solid #667eea;
            border-radius:10px;
            display:block;
            margin:20px auto;
            background:#f8f9fa
        }
        .controls {
            margin:20px 0;
            display:grid;
            grid-template-columns:repeat(3,70px);
            grid-template-rows:repeat(2,70px);
            gap:10px;
            justify-content:center
        }
        .btn {
            background:#667eea;
            color:#fff;
            border:none;
            border-radius:10px;
            font-size:28px;
            cursor:pointer;
            transition:all 0.2s;
            user-select:none
        }
        .btn:hover {background:#5568d3;transform:scale(1.05)}
        .btn:active {transform:scale(0.95)}
        #up {grid-column:2;grid-row:1}
        #left {grid-column:1;grid-row:2}
        #down {grid-column:2;grid-row:2}
        #right {grid-column:3;grid-row:2}
        .restart {
            margin-top:20px;
            padding:15px 30px;
            background:#28a745;
            color:#fff;
            border:none;
            border-radius:10px;
            font-size:18px;
            cursor:pointer
        }
        .restart:hover {background:#218838}
    </style>
</head>
<body>
    <div class="game">
        <h1>🐍 Змейка</h1>
        <div class="score">Счёт: <span id="score">0</span></div>
        <canvas id="c" width="400" height="400"></canvas>
        
        <div class="controls">
            <button class="btn" id="up">⬆️</button>
            <button class="btn" id="left">⬅️</button>
            <button class="btn" id="down">⬇️</button>
            <button class="btn" id="right">➡️</button>
        </div>
        
        <button class="restart" onclick="restart()">🔄 Начать заново</button>
        <p style="color:#6c757d;margin-top:15px">Управление: стрелки или кнопки</p>
    </div>

    <script>
        const canvas = document.getElementById('c');
        const ctx = canvas.getContext('2d');
        const scoreEl = document.getElementById('score');
        
        const SIZE = 20;
        const W = canvas.width / SIZE;
        
        let snake, food, dx, dy, score, loop;
        
        function init() {
            snake = [{x: 10, y: 10}];
            food = {x: 15, y: 15};
            dx = 0;
            dy = 0;
            score = 0;
            scoreEl.textContent = 0;
        }
        
        function draw() {
            // Очистка
            ctx.fillStyle = '#f8f9fa';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Движение
            if (dx || dy) {
                const head = {x: snake[0].x + dx, y: snake[0].y + dy};
                snake.unshift(head);
                
                // Еда
                if (head.x === food.x && head.y === food.y) {
                    score++;
                    scoreEl.textContent = score;
                    food = {
                        x: Math.floor(Math.random() * W),
                        y: Math.floor(Math.random() * W)
                    };
                } else {
                    snake.pop();
                }
                
                // Столкновение
                if (head.x < 0 || head.x >= W || head.y < 0 || head.y >= W ||
                    snake.slice(1).some(s => s.x === head.x && s.y === head.y)) {
                    clearInterval(loop);
                    alert('Игра окончена! Счёт: ' + score);
                    return;
                }
            }
            
            // Змейка
            snake.forEach((s, i) => {
                ctx.fillStyle = i === 0 ? '#667eea' : '#764ba2';
                ctx.fillRect(s.x * SIZE, s.y * SIZE, SIZE - 2, SIZE - 2);
            });
            
            // Еда
            ctx.fillStyle = '#28a745';
            ctx.beginPath();
            ctx.arc(
                food.x * SIZE + SIZE/2,
                food.y * SIZE + SIZE/2,
                SIZE/2 - 2,
                0,
                Math.PI * 2
            );
            ctx.fill();
        }
        
        function turn(ndx, ndy) {
            if (ndx && !dx) { dx = ndx; dy = 0; }
            if (ndy && !dy) { dy = ndy; dx = 0; }
        }
        
        function restart() {
            clearInterval(loop);
            init();
            loop = setInterval(draw, 100);
        }
        
        // Кнопки
        document.getElementById('up').onclick = () => turn(0, -1);
        document.getElementById('down').onclick = () => turn(0, 1);
        document.getElementById('left').onclick = () => turn(-1, 0);
        document.getElementById('right').onclick = () => turn(1, 0);
        
        // Клавиши
        document.onkeydown = e => {
            if (e.key === 'ArrowUp') turn(0, -1);
            if (e.key === 'ArrowDown') turn(0, 1);
            if (e.key === 'ArrowLeft') turn(-1, 0);
            if (e.key === 'ArrowRight') turn(1, 0);
            e.preventDefault();
        };
        
        // Старт
        init();
        loop = setInterval(draw, 100);
    </script>
</body>
</html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5025, debug=False)
