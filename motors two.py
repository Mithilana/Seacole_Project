from time import sleep
from guizero import App, Text, PushButton
from gpiozero import Robot, LED

motor = Robot(left=(4, 14), right=(17, 18))
motorSwitch = LED(27)

app = App(title="GUI Development", layout="grid", height=600, width=800)
message = Text(app, text="Dual Motor Control Interface", grid=[4,0])


motorSpeedLeft = 0
motorSpeedRight = 0


def toggleSwitch():
    if button0.text=="Start":
        motorSwitch.on()
        button0.text="Stop"
    elif button0.text == "Stop":
        motorSwitch.off()
        motor.stop()
        global motorSpeedLeft
        global motorSpeedRight
        motorSpeedLeft = 0
        motorSpeedRight = 0
        button0.text = "Start"

#Left Motor


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
    
#Right Motor
    
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

Text(app, "Motor",grid=[2,1])
button0 = PushButton(app, command=toggleSwitch, text="Start", width=10,height=3, grid=[2,4])
button1 = PushButton(app, command=LeftSpeedIncrease, text="Left +", width=10,height=3, grid=[1,3])
button2 = PushButton(app, command=LeftSpeedDecrease, text="Left -", width=10,height=3, grid=[1,5])
button3 = PushButton(app, command=RightSpeedIncrease, text = "Right +", width=10,height=3, grid=[3,3])
button4 = PushButton(app, command=RightSpeedDecrease, text="Right -", width=10, height=3, grid=[3,5])

app.display()
