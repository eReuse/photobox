import picamera

camera = picamera.PiCamera()  #Aqui se crea un componente llamado camera y se le asigna la Picamera.

camera.resolution = (1920, 1080)  #Aqui definimos la resolucion que deseamos utilizar.

def takePicture(code,loc,num):  #En este metodo, la camara toma una foto, la nombra y la guarda en una ubicación determinada. Todo definido en el archivo config.

	#AUTOMATICAMENTE PONE NOMBRE DEL 00 AL 99. Y LA UBICACION
	if num <= 10:
		camera.capture(loc + str(code) + '_' + str(num) + '.jpg')
	else:
		camera.capture(loc + str(code) + '_' + str(num) + '.jpg')
	#print("tomando fotos")

    
    
