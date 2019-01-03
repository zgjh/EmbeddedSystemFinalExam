import RPi.GPIO as GPIO
import sys
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)  #led
GPIO.output(7,GPIO.LOW)
while True:
        GPIO.output(7,GPIO.HIGH)
        print('Current LED is ON.')
        time.sleep(0.5)
        GPIO.output(7,GPIO.LOW)
        print('Current LED is OFF.')
        time.sleep(0.5)
