#el siguiente programa hara un modelo para reconocer las caras


#importamos lbrerias
import cv2
import os
import numpy as np

#indicamos una ruta enj donde estaran las imagenes de las personas
dataPath = 'F:/usuarios/alumno/Escritorio/prueba - copia/images'
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)

#le pondremos etiquetas a las imagenes asi el programa entendera que se trata de varias personas
labels = []
facesData = []
label = 0

#"leemos" todas las imagenes y les pondremos sus respectivas etiquetas
for nameDir in peopleList:
    personPath = dataPath + '/' + nameDir
    print('Leyendo las imágenes')

    for fileName in os.listdir(personPath):
        print('Rostros: ', nameDir + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+'/'+fileName,0))
    label = label + 1

#creacion de un modelo con las imagenes etiquetadas
Recognition = cv2.face.LBPHFaceRecognizer_create ()


print("Entrenando...")
Recognition.train(facesData, np.array(labels))


Recognition.write('modeloLBPHFace.xml')
print("Modelo almacenado...")