from pathlib import Path

import picamera

import config
import waitInput

camera = picamera.PiCamera()
camera.resolution = (1600, 1200)
device = 0
while True:
    device += 1
    input('Press enter to scan a new device.')
    for i in range(config.numSteps):
        pic_name = '{}-{}.jpg'.format(device, i)
        print('Press button to take picture {}'.format(pic_name))
        buttonPressed = waitInput.click()
        camera.capture(str(Path.home() / 'Pictures' / pic_name))
