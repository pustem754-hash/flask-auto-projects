#!/usr/bin/env python3
from flask import Flask, render_template_string, request, redirect
import os
from datetime import datetime
app = Flask(__name__)
db = {"posts": [], "residents": []}
HTML = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>Система учёта жильцов ЖКХ</title><style>body{font-family:Arial;background:linear-gradient(135deg,#667eea,#764ba2);min-height:100vh;padding:20px}.container{max-width:1200px;margin:0 auto;background:white;border-radius:20px;padding:40px}h1{color:#667eea;text-align:center}.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;margin:40px 0}.stat-card{background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:30px;border-radius:15px;text-align:center}.stat-card h3{font-size:2.5em}.section{margin:40px 0;padding:30px;background:#f8f9fa;border-radius:15px;border-left:5px solid #667eea}.section h2{color:#667eea;margin-bottom:20px}input,textarea{width:100%;padding:12px;border:2px solid #e0e0e0;border-radius:10px;margin-bottom:15px}button{background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:15px 40px;border:none;border-radius:10px;cursor:pointer;font-size:18px}.item{background:white;padding:25px;border-radius:12px;margin:20px 0;box-shadow:0 4px 15px rgba(0,0,0,0.1)}.item h3{color:#667eea;margin-bottom:15px}.empty{text-align:center;color:#999;padding:40px}</style></head><body><div class="container"><h1>🏢 Система учёта жильцов ЖКХ</h1><div class="stats"><div class="stat-card"><h3>{{ len(db["residents"]) }}</h3><p>Жильцов</p></div><div class="stat-card"><h3>{{ len(db["posts"]) }}</h3><p>Записей</p></div><div class="stat-card"><h3>0</h3><p>Платежей</p></div></div><div class="section"><h2>➕ Добавить запись</h2><form action="/add" method="POST"><input name="title" placeholder="Заголовок" required><textarea name="content" rows="4" placeholder="Содержание" required></textarea><button>Опубликовать</button></form></div><div class="section"><h2>📋 Записи</h2>{{ posts }}</div><div class="section"><h2>👥 Добавить жильца</h2><form action="/add_resident" method="POST"><input name="name" placeholder="ФИО" required><input name="apartment" placeholder="Квартира" required><input name="phone" placeholder="Телефон" required><button>Добавить</button></form></div><div class="section"><h2>👥 Жильцы</h2>{{ residents }}</div></div></body></html>"""
@app.route("/")
def index():
    posts = "".join([f'<div class="item"><h3>{p["title"]}</h3><p>{p["content"]}</p><small>{p["date"]}</small></div>' for p in db["posts"]]) or '<div class="empty">Записей нет</div>'
    residents = "".join([f'<div class="item"><h3>{r["name"]}</h3><p>🏠 {r["apartment"]}</p><p>📞 {r["phone"]}</p></div>' for r in db["residents"]]) or '<div class="empty">Жильцов нет</div>'
    return render_template_string(HTML, posts=posts, residents=residents)
@app.route("/add", methods=["POST"])
def add():
    db["posts"].append({"title": request.form["title"], "content": request.form["content"], "date": datetime.now().strftime("%Y-%m-%d %H:%M")})
    return redirect("/")
@app.route("/add_resident", methods=["POST"])
def add_res():
    db["residents"].append({"name": request.form["name"], "apartment": request.form["apartment"], "phone": request.form["phone"]})
    return redirect("/")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5013)), debug=False)
