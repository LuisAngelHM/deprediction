import tensorflow as tf
from tensorflow.python.client import device_lib
from tensorflow.keras.models import load_model
import cv2
import numpy as np

class Inteligencia_Artificial():
    def __init__(self) -> None:
         self.diagnostico = ""

    def setDiagnostico(self,diagnostico):
        self.diagnostico = diagnostico

    def getDiagnostico(self):
        return self.diagnostico

    def realizarDiagnostico(self,imagen_tratada):
        model = load_model("models/model_deprecnn.h5")
        prediction = model.predict(imagen_tratada)
        prediction = prediction * 100
        if (prediction[0][1] + prediction[0][2] + prediction[0][3] >= 80) and(prediction[0][0]<20):
            self.setDiagnostico("Depresión Alta")
        
        if (prediction[0][1] + prediction[0][2] + prediction[0][3] < 80 and prediction[0][1] + prediction[0][2] + prediction[0][3]>=60)  and(prediction[0][0]>20 and prediction[0][0]<=40):
            self.setDiagnostico("Depresión media")

        if (prediction[0][1] + prediction[0][2] + prediction[0][3] < 60 and prediction[0][1] + prediction[0][2] + prediction[0][3]>=30)  and(prediction[0][0]>40 and prediction[0][0]<=70):
            self.setDiagnostico("Depresión baja")
      
        if (prediction[0][1] + prediction[0][2]  + prediction[0][3] < 30) and(prediction[0][0]>=70):
            self.setDiagnostico("Sin depresión")

        return prediction

    def deteccionRostro(self,imagen):
        crop_img = None
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceClassif.detectMultiScale(imagen,
                                            scaleFactor=1.1,
                                            minNeighbors=5,
                                            minSize=(30,30),
                                            maxSize=(200,200))

        if len(faces) != 0:
            x = faces[0][0]
            y = faces[0][1]
            w = faces[0][2]
            h = faces[0][3]
            crop_img = imagen[y:y+h, x:x+w]
        return crop_img
        
    def tratamientoDeImagen(self, fotografia):
        img = cv2.cvtColor(fotografia, cv2.COLOR_RGB2GRAY)
        img = cv2.resize(src=img, dsize=(48,48),interpolation=cv2.INTER_LANCZOS4)
        img = cv2.equalizeHist(img)
        cv2.imshow("img", img)
        img = np.array(img).reshape(1,48,48,1)
        return img


