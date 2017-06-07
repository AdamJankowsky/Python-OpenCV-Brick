import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)

def update(angle):
    duty = float(angle) / 18.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    print(duty)
    time.sleep(1)


