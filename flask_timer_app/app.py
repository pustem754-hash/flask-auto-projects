from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import threading
import time

app = Flask(__name__)

# Глобальные переменные для хранения состояния таймера
timer_state = {
 'active': False,
 'start_time': None,
 'duration': 0,
 'remaining': 0
}

def update_timer():
 """Обновляет состояние таймера каждую секунду"""
 while True:
 if timer_state['active'] and timer_state['remaining'] > 0:
 timer_state['remaining'] -= 1
 if timer_state['remaining'] <= 0:
 timer_state['active'] = False
 print("Таймер завершен!")
 time.sleep(1)

# Запускаем фоновый поток для обновления таймера
timer_thread = threading.Thread(target=update_timer, daemon=True)
timer_thread.start()

@app.route('/')
def index():
 """Главная страница с таймером"""
 return render_template('index.html')

@app.route('/start_timer', methods=['POST'])
def start_timer():
 """Запускает таймер"""
 data = request.get_json()
 minutes = int(data.get('minutes', 0))
 seconds = int(data.get('seconds', 0))
 
 total_seconds = minutes * 60 + seconds
 
 if total_seconds > 0:
 timer_state['active'] = True
 timer_state['start_time'] = datetime.now()
 timer_state['duration'] = total_seconds
 timer_state['remaining'] = total_seconds
 
 return jsonify({
 'success': True,
 'message': f'Таймер запущен на {total_seconds} секунд'
 })
 else:
 return jsonify({
 'success': False,
 'message': 'Укажите время больше 0'
 })

@app.route('/stop_timer', methods=['POST'])
def stop_timer():
 """Останавливает таймер"""
 timer_state['active'] = False
 timer_state['remaining'] = 0
 
 return jsonify({
 'success': True,
 'message': 'Таймер остановлен'
 })

@app.route('/get_status')
def get_status():
 """Возвращает текущее состояние таймера"""
 return jsonify({
 'active': timer_state['active'],
 'remaining': timer_state['remaining'],
 'duration': timer_state['duration'],
 'finished': timer_state['remaining'] == 0 and not timer_state['active']
 })

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0', port=5005)