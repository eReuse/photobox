from pathlib import Path

import picamera

import config
import waitInput

camera = picamera.PiCamera()
camera.resolution = (1600, 1200)

while True:
    url = input('Waiting for QR code...')
    print('Read text: {}'.format(url))
    try:
        code = int(url[url.rfind('-') + 1:])
    except ValueError:
        print('QR is not a valid Devicehub URL.')
    else:
        print('QR is {}'.format(code))
        for i in range(config.numSteps):
            pic_name = '{}-{}.jpg'.format(code, i)
            print('Press button to take picture {}'.format(pic_name))
            buttonPressed = waitInput.click()
            camera.capture(Path.home() / 'Pictures' / pic_name)
