#el siguiente programa detectara y mostrara el nombre de la persona en pantalla 


#importamos librerias
import cv2
import os

#from pyfirmata import Arduino
#from time import sleep
from pyfirmata import Arduino, SERVO, util
import time
from datetime import date, datetime


VERDE= 3
ROJO=4
AMARILLO=2
arduino = Arduino("COM6")  #declaracion puerto serie
arduino.digital[5].mode = SERVO
time.sleep(1)

#declaracion de variables globales
numero = 0
num=0
number= 0
nm=0

today = date.today()
now = datetime.now()
dias=1

#creamos una ruta de las personas con las caras
dataPath = 'F:/usuarios/alumno/Escritorio/prueba - copia/images'
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)



#leemos el modelo que se guardo en el programa anterior
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('modeloLBPHFace.xml')

#seleccionamos la camara
cap = cv2.VideoCapture(0)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')


while True:                                             #se pregunta si la camara se puede utilizar
#se captura la imagen y se muestra en pantalla 
#        arduino.digital[5].write(1)
        arduino.digital[ROJO].write(0)
        arduino.digital[VERDE].write(0)
        arduino.digital[AMARILLO].write(1)
        ret,frame = cap.read()
        cv2.imshow("frame", frame)
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
#    arduino.digital[ROJO].write(0)
#    arduino.digital[VERDE].write(0)
#    arduino.digital[AMARILLO].write(1)
    
    

        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
                result = face_recognizer.predict(rostro)
        
        
#        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

                
                if result[1] < 57:     #si el valor de confianza es menor a 57, se dice que la persona es la correcta con el modelo
                        arduino.digital[5].write(179)
                        arduino.digital[VERDE].write(1) #prende led   
                        arduino.digital[ROJO].write(0)
                        arduino.digital[AMARILLO].write(0)  
                        
                        etiqueta = "{}".format(imagePaths[result[0]])
                        cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)  #se muestra el nombre de la persona
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

                        def current_date_format(date):
                                months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
                                day = date.day
                                month = months[date.month - 1]
                                year = date.year
                                hour = now.hour 
                                minute = now.minute
                                seconds = now.second
                                messsage = "{} de {} del {} a las {},{},{} hs".format(day, month, year, hour, minute, seconds)
                                for dia in range(date.day):
                                        f = open("F:/usuarios/alumno/Escritorio/prueba - copia/" + etiqueta + str(".txt"), "a")
                                        if now.hour <= 11:
                                                print("que tengas buen dia")
                                                f.write(messsage)                             
                                                f.write('\n' + messsage)
                                                f.close()
                                        elif dia == 29:
                                                import Enviar_Mail 
                                        else:
                                                print("ya registrado")
                                                f.write(messsage)                             
                                                f.write('\n' + messsage)
                                                f.close()
                                return messsage

                        now = datetime.now()
                        print(current_date_format(now))





                else:                         #si el valor de confianza, supera los 57, se dice que la persona es desconocida o no reconocido
                        arduino.digital[VERDE].write(0)
                        arduino.digital[ROJO].write(1)
                        arduino.digital[AMARILLO].write(0)
                        arduino.digital[5].write(1)
                        #se toma un registro del dia en el que se intento reconocer
                     
                        cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                        cv2.imwrite("F:/usuarios/alumno/Escritorio/prueba - copia/desconocidos/"+ str("desconocido") + str(num) + ".jpg", gray)    #se toma una captura para que quede registrado
                        def current_date_format(date):
                                months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
                                day = date.day
                                month = months[date.month - 1]
                                year = date.year
                                hour = now.hour 
                                minute = now.minute
                                seconds = now.second
                                messsage = "{} de {} del {} a las {},{},{} hs".format(day, month, year, hour, minute, seconds)
                                f = open("F:/usuarios/alumno/Escritorio/prueba - copia/" + etiqueta + str(".txt"), "w")
                                f = open ("desconocido.txt", "w")
                                f.write("desconocido" + str(messsage))
                                f.close()
                                return messsage


#                arduino.digital[LED].write(0) #prende led                  
                cv2.imshow('frame',frame)
        k = cv2.waitKey(1)
        if k == 27:
                arduino.digital[VERDE].write(0) #prende led   
                arduino.digital[ROJO].write(0)
                arduino.digital[AMARILLO].write(0)  
                arduino.digital[5].write(1)
                break
cap.release()
cv2.destroyAllWindows()