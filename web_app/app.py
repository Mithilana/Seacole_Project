from flask import Flask, render_template
from time import sleep
from gpiozero import Robot, Motor

app = Flask(__name__, static_folder='data',static_url_path='/data')

motor = Robot(left=(4, 14), right=(17, 18))
motorSpeedLeft = 0
motorSpeedRight = 0

f = open('data/speed_logs.txt','w')
f.write("Activating motors... \n")
f.close()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/log')
def log():
    return render_template('log.html')

@app.route('/stop')
def toggleSwitch():
    global motorSpeedLeft
    global motorSpeedRight
    motorSpeedRight = 0
    motorSpeedLeft = 0
    motor.stop()
    print("Stopping motors")
    f = open('data/speed_logs.txt','a')
    f.write(f"Stopped motors\n")
    f.close()
    return render_template('index.html')

#Left Motor
@app.route('/leftinc')
def LeftSpeedIncrease():
    global motorSpeedLeft
    motorSpeedLeft += 0.1
    if motorSpeedLeft >= 1:
        motorSpeedLeft = 1
    if motorSpeedLeft >= 0:
        motor.left_motor.forward(speed=motorSpeedLeft) 
    elif motorSpeedLeft < 0:
        motor.left_motor.backward(speed=abs(motorSpeedLeft)) 
    print("Increased speed of left motor. Current speed = ", round(motorSpeedLeft, 1))
    f = open('data/speed_logs.txt','a')
    f.write(f"Set left speed: {motorSpeedLeft}\n")
    f.close()
    return render_template('index.html')

@app.route('/leftdec')
def LeftSpeedDecrease():
    global motorSpeedLeft
    motorSpeedLeft -= 0.1
    if motorSpeedLeft >= 1:
        motorSpeedLeft = 1
    if motorSpeedLeft >= 0:
        motor.left_motor.forward(speed=motorSpeedLeft) 
    elif motorSpeedLeft < 0:
        motor.left_motor.backward(speed=abs(motorSpeedLeft))
    print("Decreased speed of left motor. Current speed = ", round(motorSpeedLeft, 1))
    f = open('data/speed_logs.txt','a')
    f.write(f"Set left speed: {motorSpeedLeft}\n")
    f.close()
    return render_template('index.html')


#Right Motor
@app.route('/rightinc')    
def RightSpeedIncrease():
    global motorSpeedRight
    motorSpeedRight += 0.1
    if motorSpeedRight >= 1:
        motorSpeedRight = 1
    if motorSpeedRight >= 0:
        motor.right_motor.forward(speed=motorSpeedRight) 
    elif motorSpeedRight < 0:
        motor.right_motor.backward(speed=abs(motorSpeedRight))
    print("Increased speed of right motor. Current speed = ", round(motorSpeedRight, 1))
    f = open('data/speed_logs.txt','a')
    f.write(f"Set left speed: {motorSpeedRight}\n")
    f.close()
    return render_template('index.html')

@app.route('/rightdec')    
def RightSpeedDecrease():
    global motorSpeedRight
    motorSpeedRight -= 0.1
    if motorSpeedRight >= 1:
        motorSpeedRight = 1
    if motorSpeedRight >= 0:
        motor.right_motor.forward(speed=motorSpeedRight) 
    elif motorSpeedRight < 0:
        motor.right_motor.backward(speed=abs(motorSpeedRight))
    print("Decreased speed of right motor. Current speed = ", round(motorSpeedRight, 1))
    f = open('data/speed_logs.txt','a')
    f.write(f"Set right speed: {motorSpeedRight}\n")
    f.close()
    return render_template('index.html')

@app.route('/forward')
def forward():
    global motorSpeedLeft
    global motorSpeedRight
    motorSpeedLeft = min(motorSpeedRight,motorSpeedLeft)
    motorSpeedRight = motorSpeedLeft
    LeftSpeedIncrease()
    RightSpeedIncrease()
    return render_template('index.html')

@app.route('/backward')
def backward():
    global motorSpeedLeft
    global motorSpeedRight
    motorSpeedLeft = min(abs(motorSpeedRight),abs(motorSpeedLeft))
    motorSpeedRight = motorSpeedLeft
    LeftSpeedDecrease()
    RightSpeedDecrease()
    return render_template('index.html')

@app.route('/leftturn')
def leftturn():
    LeftSpeedDecrease()
    RightSpeedIncrease()
    return render_template('index.html')

@app.route('/rightturn')
def rightturn():
    LeftSpeedIncrease()
    RightSpeedDecrease()
    return render_template('index.html')

@app.after_request
def add_header(response):
    response.headers['Cache-Control']='no-store'
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0")