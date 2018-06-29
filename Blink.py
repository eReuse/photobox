import RPi.GPIO as GPIO
import time


def setup():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(26,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)

def ledOn(led)

    if(led == 1)
        GPIO.output(26,GPIO.HIGH)
        print "LED 1 ON"
    else
        GPIO.output(25,GPIO.HIGH)
        print "LED 1 ON"





"""print "LED off"
time.sleep(1)
GPIO.output(26,GPIO.LOW)"""
