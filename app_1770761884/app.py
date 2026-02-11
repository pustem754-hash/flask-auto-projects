#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return """<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>✅ TODO список</title>
<style>
body{margin:0;display:flex;justify-content:center;align-items:center;min-height:100vh;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);font-family:Arial}
.container{background:#fff;padding:40px;border-radius:20px;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,0.3)}
h1{color:#667eea;margin:0 0 20px}
.badge{background:#28a745;color:#fff;padding:10px 20px;border-radius:20px;display:inline-block;margin:10px}
</style></head><body>
<div class="container">
<h1>✅ ✅ TODO список</h1>
<div class="badge">Порт: 5021</div>
<p>http://89.19.213.119:5021</p>
</div></body></html>"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5021, debug=False)
