from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-quiz-key-12345'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

questions = [
    {"q": "Сколько планет в Солнечной системе?", "options": ["7", "8", "9", "10"], "answer": "8"},
    {"q": "Столица России?", "options": ["Москва", "Санкт-Петербург", "Казань", "Екатеринбург"], "answer": "Москва"},
    {"q": "Сколько континентов на Земле?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"q": "Какой язык программирования используется для веб-разработки?", "options": ["Python", "Java", "C++", "Все вышеперечисленные"], "answer": "Все вышеперечисленные"},
    {"q": "Какой океан самый большой?", "options": ["Атлантический", "Индийский", "Тихий", "Северный Ледовитый"], "answer": "Тихий"}
]

@app.route('/')
def index():
    session.clear()
    return render_template('index.html', total=len(questions))

@app.route('/question/<int:q_id>', methods=['GET', 'POST'])
def question(q_id):
    if q_id >= len(questions):
        return redirect(url_for('results'))
    
    if request.method == 'POST':
        if 'score' not in session:
            session['score'] = 0
        answer = request.form.get('answer')
        if answer == questions[q_id]['answer']:
            session['score'] += 1
        return redirect(url_for('question', q_id=q_id + 1))
    
    return render_template('question.html', 
                         question=questions[q_id], 
                         q_id=q_id, 
                         question_num=q_id+1,
                         total=len(questions))

@app.route('/results')
def results():
    score = session.get('score', 0)
    total = len(questions)
    percentage = (score / total) * 100
    
    if percentage >= 80:
        result_text = "Отлично!"
        result_class = "excellent"
    elif percentage >= 60:
        result_text = "Хорошо!"
        result_class = "good"
    elif percentage >= 40:
        result_text = "Неплохо!"
        result_class = "average"
    else:
        result_text = "Нужно подучиться!"
        result_class = "poor"
    
    return render_template('results.html', 
                         score=score, 
                         total=total, 
                         percentage=percentage, 
                         result_text=result_text, 
                         result_class=result_class)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5023, debug=True)
