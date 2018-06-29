import RPi.GPIO as GPIO
import time


def setup():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(26,GPIO.OUT) #LED DE ESTADO 'QR'
    GPIO.setup(25,GPIO.OUT) #LED DE ESTADO 'SCANNING'
    GPIO.setup(6,GPIO.OUT) #LED DEL BOTON

def ledOn(led):

    if(led == 1):
        
        GPIO.output(26,GPIO.HIGH)
        print ("LED 1 ON")
        
    elif(led == 2):
    
        GPIO.output(25,GPIO.HIGH)
        print ("LED 2 ON")
        
    else:

        GPIO.output(6,GPIO.HIGH)
        print ("LED 3 ON")
        

def ledOff(led):

    if(led == 1):
        GPIO.output(26,GPIO.LOW)
        print ("LED 1 OFF")
        
    elif(led == 2):
    
        GPIO.output(25,GPIO.LOW)
        print ("LED 2 OFF")
        
    else:

        GPIO.output(6,GPIO.LOW)
        print ("LED 3 OFF")

def ledError():
    
    counter = 0
    while(counter < 10):
    
        GPIO.output(26,GPIO.HIGH)
        print ("LED 1 ON")
        GPIO.output(25,GPIO.HIGH)
        print ("LED 2 ON")
        GPIO.output(6,GPIO.HIGH)
        print ("LED 3 ON")
        time.sleep(0.1)
        GPIO.output(26,GPIO.LOW)
        print ("LED 1 OFF")
        GPIO.output(25,GPIO.LOW)
        print ("LED 2 OFF")
        GPIO.output(6,GPIO.LOW)
        print ("LED 3 OFF")
        time.sleep(0.1)
        print ("counter:", counter)
        counter = counter + 1
        
   
        

