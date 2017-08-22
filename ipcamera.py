# Usando Una Camara IP, o la App Android IP Webcam para hacer streaming
# de video a OpenCV3 con Python2

import urllib
import cv2
import numpy as np
import time

# Reemplaza la URL por la IP y el Puerto de tu cámara
url='http://192.168.1.55:8080/shot.jpg'


while True:
    # Usa urllib para obtener la imagen de la cámara
    imgResp = urllib.urlopen(url)
    
    # Numpy para convertir la imagen en un Array
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    
    # Finalmente la decodifica en un formato que openCV entiende
    img = cv2.imdecode(imgNp,-1)
	
	
	# Muestra el Streamming de la imagen
    cv2.imshow('IPWebcam',img)

    #Si quieres reducir el procesamiento un poco
    #time.sleep(0.1) 

    # Sale del bucle si presionas 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
