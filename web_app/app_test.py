from flask import Flask, render_template
from time import sleep

app = Flask(__name__)

motorSpeedLeft = 0
motorSpeedRight = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/log')
def log():
    return render_template('log.html')

@app.route('/backward')
def backward():
    global motorSpeedLeft
    global motorSpeedRight
    motorSpeedLeft = min(motorSpeedRight,motorSpeedLeft)
    motorSpeedRight = motorSpeedLeft
    print("hi")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
