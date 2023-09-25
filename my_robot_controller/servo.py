import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50)


servo1.start(0)
time.sleep(1)

def setAngle(angle):
    duty= angle /18+2
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    angle=int(input("angle : "))
angle = int(input("angle : "))
setAngle(angle)


servo1.stop()
GPIO.cleanup()

