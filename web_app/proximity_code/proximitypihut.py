import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG_left = 23
ECHO_left = 24

GPIO.setup(TRIG_left,GPIO.OUT)
GPIO.setup(ECHO_left,GPIO.IN)

TRIG_right = 27
ECHO_right = 22

GPIO.setup(TRIG_right,GPIO.OUT)
GPIO.setup(ECHO_right,GPIO.IN)

TRIG_up = 2
ECHO_up = 3

GPIO.setup(TRIG_up,GPIO.OUT)
GPIO.setup(ECHO_up,GPIO.IN)

TRIG_down = 10
ECHO_down = 9 

GPIO.setup(TRIG_down,GPIO.OUT)
GPIO.setup(ECHO_down,GPIO.IN)

def distance(TRIG, ECHO):

    GPIO.output(TRIG, False)
    time.sleep(1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()      

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

if __name__ == '__main__':
    try:
        f = open('data/prox_logs.txt', 'w')
        f.write("Activating proximity sensors\n")
        f.close()
        while True:
            distleft = distance(TRIG_left, ECHO_left)
            distright = distance(TRIG_right, ECHO_right)
            distup = distance(TRIG_up, ECHO_up)
            distdown = distance(TRIG_down, ECHO_down)
            if distleft > 2000 or distleft < 5:
                distleft = 0
            if distright > 2000 or distright < 5:
                distright = 0
            if distup > 2000 or distup < 5:
                distup = 0
            if distdown > 2000 or distdown < 5:
                distdown = 0 

            print(f"Distance Left = {distleft:.1f} cm   Distance Right = {distright:.1f}cm   Distance Up = {distup:.1f}cm   Distance Down = {distdown:.1f}cm")
            f = open('data/prox_logs.txt', 'a')
            f.write(f"Distance Left = {distleft:.1f} cm   Distance Right = {distright:.1f}cm   Distance Up = {distup:.1f}cm   Distance Down = {distdown:.1f}cm\n")
            f.close()
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()


