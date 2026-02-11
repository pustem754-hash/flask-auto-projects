#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return """<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>🐍 Змейка</title>
<style>
body{margin:0;display:flex;justify-content:center;align-items:center;min-height:100vh;background:linear-gradient(135deg,#667eea,#764ba2);font-family:Arial}
.game{background:#fff;padding:30px;border-radius:20px;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,0.3)}
h1{color:#667eea;margin:0 0 20px}
canvas{border:3px solid #667eea;border-radius:10px;display:block;margin:20px auto}
.score{font-size:24px;color:#495057;margin:10px}
.btn{background:#667eea;color:#fff;border:none;padding:15px 30px;border-radius:10px;font-size:18px;cursor:pointer;margin:10px}
.btn:hover{background:#5568d3}
</style></head><body>
<div class="game">
<h1>🐍 Змейка</h1>
<div class="score">Счёт: <span id="score">0</span></div>
<canvas id="c" width="400" height="400"></canvas>
<button class="btn" onclick="restart()">🔄 Начать заново</button>
<p style="color:#6c757d">Управление: ⬆️⬇️⬅️➡️</p>
</div>
<script>
const c=document.getElementById('c'),ctx=c.getContext('2d'),s=20,tc=c.width/s;
let snake=[{x:10,y:10}],food={x:15,y:15},dx=0,dy=0,score=0,loop;
function draw(){
ctx.fillStyle='#f8f9fa';ctx.fillRect(0,0,c.width,c.height);
if(dx||dy){
const h={x:snake[0].x+dx,y:snake[0].y+dy};
snake.unshift(h);
if(h.x===food.x&&h.y===food.y){score++;document.getElementById('score').textContent=score;food={x:Math.floor(Math.random()*tc),y:Math.floor(Math.random()*tc)};}
else snake.pop();
if(h.x<0||h.x>=tc||h.y<0||h.y>=tc||snake.slice(1).some(seg=>seg.x===h.x&&seg.y===h.y)){clearInterval(loop);alert('Игра окончена! Счёт: '+score);return}}
snake.forEach((seg,i)=>{ctx.fillStyle=i===0?'#667eea':'#764ba2';ctx.fillRect(seg.x*s,seg.y*s,s-2,s-2)});
ctx.fillStyle='#28a745';ctx.beginPath();ctx.arc(food.x*s+s/2,food.y*s+s/2,s/2-2,0,2*Math.PI);ctx.fill()}
document.addEventListener('keydown',e=>{
if(e.key==='ArrowUp'&&dy===0){dx=0;dy=-1}
if(e.key==='ArrowDown'&&dy===0){dx=0;dy=1}
if(e.key==='ArrowLeft'&&dx===0){dx=-1;dy=0}
if(e.key==='ArrowRight'&&dx===0){dx=1;dy=0}});
function restart(){clearInterval(loop);snake=[{x:10,y:10}];dx=0;dy=0;score=0;document.getElementById('score').textContent=0;loop=setInterval(draw,100)}
loop=setInterval(draw,100);
</script></body></html>"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5024, debug=False)
