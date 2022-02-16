import cv2
from PIL import Image
class Camara:

    def tomarFotografia(cap):
        ret,frame = cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        return img
        