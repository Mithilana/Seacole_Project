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
        while True:
            distleft = distance(TRIG_left, ECHO_left)
            distright = distance(TRIG_right, ECHO_right)
            if distleft > 2000 or distleft < 5:
                distleft = 0
            if distright > 2000 or distright < 5:
                distright = 0
                
            print(f"Distance Left = {distleft:.1f} cm   Distance Right = {distright:.1f}cm   ")
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        



