from tkinter import filedialog
from PIL import Image
import cv2
class Fotografia:
    def tomarNueva(cap):
        try:
            ret,frame = cap.read()
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
        except:
            pass
        return img

    def subirExistente():
        archivo = filedialog.askopenfilename(title="Abrir imagen")
        img = Image.open(archivo)
        width, height = img.size

        if height <= width:
            ratio = height/width
            new_width = 450
            new_height = int(new_width * ratio)
            img = img.resize([new_width,new_height])
        else:
            ratio = width/height
            new_height = 430
            new_width = int(new_height * ratio)
            img = img.resize([new_width,new_height])  
        return img
