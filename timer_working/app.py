import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''<!DOCTYPE html>
<html>
<head>
<title>Timer</title>
<style>
body{margin:0;padding:50px;font-family:Arial;background:linear-gradient(135deg,#667eea,#764ba2);text-align:center}
h1{color:#fff;font-size:48px}
#timer{color:#fff;font-size:120px;font-weight:bold}
</style>
</head>
<body>
<h1>Timer</h1>
<div id="timer">60</div>
<script>
let t=60;
setInterval(()=>{t--;document.getElementById('timer').innerText=t;if(t<=0)alert('Done!')},1000);
</script>
</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5015)))
