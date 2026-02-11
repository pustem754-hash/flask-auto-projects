
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Timer started. Waiting for 60 seconds...'

@app.route('/wait')
def wait():
    time.sleep(60)
    return 'Timer finished.'

if __name__ == '__main__':
    app.run()
