#el siguiente sketch tomara fotos de la persona a reconocer


#importamos librerias
import numpy as np
import cv2
import os
import imutils
import errno


cap = cv2.VideoCapture(0)  #seleccionamos la camara
flag = cap.isOpened()      
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') 

#declaramos variables globales
count = 0
numero=0
nombre=input("nombre:")  #variable donde se almacenara el nombre de la persona
 
 
 #creacion de na carpeta con el imput
carpeta = 'F:/usuarios/alumno/Escritorio/prueba - copia/images/' + str(nombre) + str("/")
try:
    os.mkdir(carpeta)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise


while(flag):                                         #se pregunta si la camara se puede habilitar
    
    ret, frame = cap.read()  
    cv2.imshow('frame',frame)                        #se enciende la camara
    frame =  imutils.resize(frame, width=640)        #se redimensiona las captura
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #se convierte en blanco y negro las capturas
    auxFrame = gray.copy()
#    cv2.imshow("sonreir ", gray)                     #se muestra en pantalla la capturadora
    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
            k= cv2.waitKey(1)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)   #se crea un cuadro que muestre la parte que se esta tomando
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(carpeta + str(nombre) + str( numero) + ".jpg".format(count), rostro) #se guarda la imagen en su respectiva carpeta
            
            
            print("guardada con exito" + str(count))
            count = count + 1
            print("-------------------------------")
            numero += 1      
    if count >= 300:    #un total de 300 fotos, haran que se termine el programa
            break
    cv2.imshow('frame',frame) 
cap.release()
cv2.destroyAllWindows()