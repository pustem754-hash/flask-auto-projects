#!/usr/bin/env python3
from flask import Flask, render_template_string, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://zkh_user:zkh_password_2026@localhost/zkh_system"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Resident(db.Model):
    __tablename__ = "residents"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    apartment = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(255))
    balance = db.Column(db.Numeric(10, 2), default=0)

HTML = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Полная ЖКХ система</title>
<style>
* {margin:0;padding:0;box-sizing:border-box}
body {font-family:Arial;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);min-height:100vh;padding:20px}
.container {max-width:1200px;margin:0 auto;background:white;border-radius:20px;padding:30px;box-shadow:0 20px 60px rgba(0,0,0,0.3)}
h1 {color:#667eea;margin-bottom:30px;font-size:2.5em;text-align:center}
.stats {display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;margin-bottom:30px}
.stat-card {background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;padding:20px;border-radius:15px;text-align:center}
.stat-card h3 {font-size:2em;margin-bottom:10px}
table {width:100%;border-collapse:collapse;margin-top:20px}
th,td {padding:15px;text-align:left;border-bottom:1px solid #ddd}
th {background:#667eea;color:white;font-weight:600}
tr:hover {background:#f5f5f5}
.badge {padding:5px 15px;border-radius:20px;font-size:0.9em;font-weight:600}
.badge.positive {background:#4caf50;color:white}
.badge.negative {background:#f44336;color:white}
</style></head><body>
<div class="container">
<h1>🏠 Полная ЖКХ система</h1>
<div class="stats">
<div class="stat-card"><h3>{{residents|length}}</h3><p>Всего жильцов</p></div>
<div class="stat-card"><h3>{{apartments}}</h3><p>Квартир</p></div>
</div>
<h2>📋 Список жильцов</h2>
<table><thead><tr><th>ФИО</th><th>Квартира</th><th>Телефон</th><th>Email</th><th>Баланс</th></tr></thead>
<tbody>
{% for r in residents %}
<tr>
<td>{{r.full_name}}</td>
<td>{{r.apartment}}</td>
<td>{{r.phone or "-"}}</td>
<td>{{r.email or "-"}}</td>
<td>
{% if r.balance >= 0 %}
<span class="badge positive">{{r.balance}} ₽</span>
{% else %}
<span class="badge negative">{{r.balance}} ₽</span>
{% endif %}
</td>
</tr>
{% endfor %}
</tbody></table>
</div></body></html>"""

@app.route("/")
def index():
    residents = Resident.query.all()
    apartments = len(set([r.apartment for r in residents]))
    return render_template_string(HTML, residents=residents, apartments=apartments, name="Полная ЖКХ система")

@app.route("/health")
def health():
    return jsonify({"status": "ok", "app": "Полная ЖКХ система"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5016))
    app.run(host="0.0.0.0", port=port, debug=False)
