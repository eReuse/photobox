import RPi.GPIO as GPIO
from termios import tcflush, TCIFLUSH   #Importa las librerias necesarias para hacer un fush del cache.

import time
#import sys

GPIO.setmode(GPIO.BCM)  #Define un modo al pin donde esta conectado el pulsador.

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Define el pin donde va a estar conectado el boton

butonState = None  # Define una variable que obtiene el estado del boton.   

def click():

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    butonState = True       #Define el estado del boton a verdadero, es decir, no pulsado.
    
    while True: #NOS DA TIEMPO A PULSAR EL BOTON I VERLO
        input_state = GPIO.input(23)    #Declara una variable donde se asigna lo que se recibe por el input del boton

        if input_state == False:        #Si la variable del boton es falsa, el boton esta pulsado y hace lo siguiente.
            start = time.time()         #Inicializa una variable y le da el tiempo
            while (time.time() - start < 3):    #Si durante 3 segundos el boton esta pulsado
                input_state = GPIO.input(23)    #Detecta si el boton estubo pulsado mas de 3 segundos.
                if input_state == True:         #Si despues de ese tiempo el boton se libero, continua con el escanner, sino:
                    print ('Button Pressed')
                    return True
                
            print("Reseted by user!!!") #Sino, resetea y vuelve al estado principal QR.
            return False
            
        
     
    
def Reset():
    # print("Manually reseted")
    return False
