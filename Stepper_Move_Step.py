from time import sleep
import RPi.GPIO as GPIO

DIR = 20 #Direction GPIO Pin
STEP = 21 #Step GPIO Pin
CW = 1 #Clockwise Rotation
CCW = 0 #Counterclockwise Rotation
SPR = 400 # Steps per Revolution

#numSteps = 2   #This number is the number of photos and the number of steps to stop.


def moveStep(numSteps):

	print("moviendo stepper...") 
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(DIR,GPIO.OUT)
	GPIO.setup(STEP,GPIO.OUT)
	GPIO.output(DIR, CW)

	MODE = (14, 15, 18) #Microsteo Resolution GPIO Pins
	GPIO.setup(MODE, GPIO.OUT)
	RESOLUTION = {'Full' : (0, 0, 0),
		  'Half' : (1, 0, 0),
		  '1/4' : (0, 1, 0),
		  '1/8' : (1, 1, 0),
		  '1/16' : (0, 0, 1),
		  '1/32' : (1, 0, 1),}
	GPIO.output(MODE,RESOLUTION['1/32'])

	step_count = SPR * 32
	delay = .0208 / 32

	for x in range(int(step_count/numSteps)):
	    GPIO.output(STEP, GPIO.HIGH)
	    sleep(delay)
	    GPIO.output(STEP, GPIO.LOW)
	    sleep(delay)
	    
	sleep(.5)
	GPIO.cleanup()
    
def moveAll():
    
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(DIR,GPIO.OUT)
	GPIO.setup(STEP,GPIO.OUT)
	GPIO.output(DIR, CW)

	MODE = (14, 15, 18) #Microsteo Resolution GPIO Pins
	GPIO.setup(MODE, GPIO.OUT)
	RESOLUTION = {'Full' : (0, 0, 0),
		'Half' : (1, 0, 0),
		'1/4' : (0, 1, 0),
		'1/8' : (1, 1, 0),
		'1/16' : (0, 0, 1),
		'1/32' : (1, 0, 1),}
	GPIO.output(MODE,RESOLUTION['1/32'])

	GPIO.output(DIR,CCW)
    
	step_count = SPR * 32
	delay = .0208 / 32

	for x in range(int(step_count)):
	    GPIO.output(STEP, GPIO.HIGH)
	    sleep(delay)
	    GPIO.output(STEP, GPIO.LOW)
	    sleep(delay)
	    
	sleep(.5)
	GPIO.cleanup()
#moveStep(numSteps)
    
"""for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR,CCW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP,GPIO.LOW)
    sleep(delay)"""

#GPIO.cleanup()
