#!/usr/bin/python3

#Aquí importamos todas las librerias que necesitamos para correr nuestro script.
import sys
from termios import tcflush, TCIFLUSH
import config
import waitInput
import takePicture
import Thunderborg_moveStepper as ThunderBorg_moveStepper
import Led
from boltons.urlutils import URL

code = 0                #Variable que contiene el codigo recibido por el Scanner QR.
state = 'QR'            #Declara una variable de estado, con un estado QR.
actualStep = 0          #Declara la variable del paso actual en el que va.
buttonPressed = None    #Declara la variable del estado del boton y la asigna a negativo(No pulsado)
SPR = 3000              #Declara la variable de cuantos pasos tiene que dar el motor paso a paso para hacer una vuelta.

#Aqui esta el proceso del scanner para detectar el codigo QR

#Una vez se detecte el QR se encendera una luz para avisar que fue registrado el QR

#Una vez se haya colocado el objeto en el centro, se pulsara el boton para iniciar el escaneo.

def makeScan(code):
#Aqui ira la logica del movimiento del motor 1/8 de la vuelta y tomara una foto.
    
    ThunderBorg_moveStepper.MoveStep(SPR / config.numSteps)  #Llama a la libreria de la shield con el controlador de motor y le pasa el parametro de cuanto se tiene que mover.
    global actualStep                                       #Declara una variable global que es el paso actual en el que va.
    actualStep += 1                                         #Suma uno a la variable del paso acutal en el que va.
    print(actualStep)                                       #Imprime por terminal el paso actual en el que va.
    takePicture.takePicture(code,config.loc,actualStep)     #Toma una foto con la PiCamera, pasandole el codigo para poner nombre a la imagen, la localizacion de guardado y el paso actual.

print("Starting...")    #Al inicio de todo imprime por terminal que la maquina se esta inicializando...

#Aqui inicia el proceso del scanner para detectar el codigo QR
Led.setup()
while True:
    if state == 'QR':
        
        #Una vez se detecte el QR se encendera una luz para avisar que fue registrado el QR
        # led 1 on, led 2 off
        Led.ledOn(1)
        Led.ledOff(2)
        Led.ledOff(3)
        
        print("Waiting for QR code")

        # limpia el buffer de input
        tcflush(sys.stdin, TCIFLUSH)

        #ESTO HAY QUE CAMBIARLO PARA QUE NO SEA UN NUMERO, SEA UNA URL.
        url = input()
        print('Read text: {}'.format(url))
        try:
            code = int(URL(url).path_parts[-1])
            if config.code_min < code < config.code_max:
                raise ValueError()
        except ValueError:
            print('QR is not a valid Devicehub URL.')
            Led.ledError()
            code = 0
            state = "QR"
        else:
            state = 'SCAN' #Pasa al estado de Scan.
    elif state == 'SCAN':  #Si no esta en estado QR, entra en estado SCAN.

        # led 2 on, led 1 off
        
        Led.ledOff(1)
        Led.ledOff(2)
        Led.ledOn(3)
        
        print("Waiting for button press") #Imprime por terminal que espera a que se pulse el boton.

        buttonPressed = waitInput.click() # Detecta si el boton fué pulsado y como. Si solo fue pulsado procede, si se pulsa 3 segundos, Reinicia.
        
        if buttonPressed: #Si el boton fue pulsado se prepara para hacer el Scan.
            
            Led.ledOff(1)
            Led.ledOn(2)
            Led.ledOff(3)
            
            actualStep = 0    #Inicializa la variable de en que foto está.
            
            for num in range(0,config.numSteps): # Aqui se automatiza cuantas fotos se hara dependiendo del archivo de configuración.
                if actualStep <= config.numSteps: #Si aun quedan fotos por hacer, las hace.
                    if code > 0: makeScan(code)   #Si el paso en el que está es mayor que 0, hace el siguiente paso.
                    else:                       # Comprueba que el paso en el que esta no sea negativo, si lo es da fallo y resetea.
                        print("2 QR code ERROR!!")
                        Led.ledError()
                        code = 0
                        state = "QR"
            print("Finished photos")  #Cuando ya no quedan mas fotos por hacer, imprime por la terminal que se acabaron de hacer las fotos.
            state = "QR"            # Ha acabado y vuelve al estado inicial QR para detectar el siguiente objeto.
            
        else:                   #Si el codigo es 0, resetea volviendo al estado QR (Es para evitar errores).
            code = 0
            state = "QR"

