#!/usr/bin/env python3
from flask import Flask, render_template_string, request, redirect
from datetime import datetime
import os

app = Flask(__name__)
db = {"posts": [], "comments": {}}

@app.route('/')
def index():
    h = """<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><title>Блог ЖКХ</title>
<style>*{margin:0;padding:0}body{font-family:Arial;background:linear-gradient(135deg,#667eea,#764ba2);min-height:100vh;padding:20px}.container{max-width:1200px;margin:0 auto;background:white;padding:40px;border-radius:20px}h1{color:#667eea;text-align:center;margin-bottom:30px}h2{color:#764ba2;margin:25px 0 15px}.form-group{margin-bottom:20px}label{display:block;margin-bottom:8px}input,textarea{width:100%;padding:12px;border:2px solid #667eea;border-radius:10px;font-size:16px}textarea{min-height:120px}button{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;padding:15px 30px;border-radius:10px;cursor:pointer;font-size:16px;font-weight:bold}.item{background:#f8f9fa;padding:20px;margin:15px 0;border-radius:10px;border-left:4px solid #667eea}.item h3{color:#667eea}.meta{color:#666;font-size:14px;margin-top:10px}.comment{background:#e9ecef;padding:15px;margin:10px 0 10px 30px;border-radius:8px}.empty{text-align:center;color:#999;padding:40px}</style></head><body><div class="container">
<h1>📝 Блог ЖКХ</h1><h2>Новый пост</h2><form method="POST" action="/add">
<div class="form-group"><label>Заголовок:</label><input name="title" required></div>
<div class="form-group"><label>Содержание:</label><textarea name="content" required></textarea></div>
<div class="form-group"><label>Автор:</label><input name="author" value="Администратор"></div>
<button>Опубликовать</button></form><h2>Все посты</h2>
{% if not posts %}<p class="empty">Нет постов</p>{% else %}
{% for i,p in enumerate(posts) %}<div class="item"><h3>{{p['title']}}</h3><p>{{p['content']}}</p>
<div class="meta">{{p['author']}} | {{p['date']}}</div>
<form method="POST" action="/c/{{i}}"><input name="text" placeholder="Комментарий..."><button>Отправить</button></form>
{% if i in comments %}{% for c in comments[i] %}<div class="comment">💬 {{c}}</div>{% endfor %}{% endif %}
</div>{% endfor %}{% endif %}</div></body></html>"""
    return render_template_string(h, posts=db["posts"], comments=db["comments"], enumerate=enumerate)

@app.route('/add', methods=['POST'])
def add():
    db["posts"].append({"title":request.form['title'],"content":request.form['content'],"author":request.form['author'],"date":datetime.now().strftime('%d.%m.%Y %H:%M')})
    return redirect('/')

@app.route('/c/<int:i>', methods=['POST'])
def com(i):
    if i not in db["comments"]: db["comments"][i]=[]
    db["comments"][i].append(request.form['text'])
    return redirect('/')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5011)), debug=False)
