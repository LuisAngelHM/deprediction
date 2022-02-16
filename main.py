from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from clases.fotografia import Fotografia
from clases.usuario import Usuario
import cv2
import numpy as np

ventana = Tk()
label_la = Label(ventana)
cap  = cv2.VideoCapture(0)
live_view = True
imagen = None
subir_foto = True
tomar_foto = True
label_img = Label(ventana)

def stop_camara():
    global tomar_foto, cap, subir_foto
    if tomar_foto is True:
        global live_view
        live_view = False
    else: 
        cap  = cv2.VideoCapture(0)
        live_view = True
        tomar_foto = True
        tomar_imagen()
        
        
        


def tomar_imagen():
    global label_la, label_img, tomar_foto, subir_foto
    global imagen
    if subir_foto is False:
         label_img.place_forget()
    img = Fotografia.tomarNueva(cap)
    if live_view:   
        imgtk = ImageTk.PhotoImage(image=img)
        label_la.imgtk = imgtk
        label_la.configure(image=imgtk)
        label_la.place(x=50, y=90)
        label_la.after(10, tomar_imagen)
    else:
        cap.release()
        imagen = np.asarray(img)
        diagnostico()
        tomar_foto = False
        subir_foto = True

       


def mostrar_imagen():
    global cap, imagen, subir_foto, tomar_foto
    global label_la
    tomar_foto = False
    if subir_foto is True:
        label_la.place_forget()
        cap.release()
    else:
        label_img.place_forget()
    img = Fotografia.subirExistente()
    ven_img = ImageTk.PhotoImage(img)
    label_img.config(image=ven_img)
    label_img.place(x=50, y=100)
    img = np.asarray(img)
    imagen = img
    subir_foto = False
    diagnostico()
    ventana.mainloop()


def diagnostico():
    user = Usuario()
    user.setFotografia(imagen)
    resultado, probabilidad = user.IniciarDiagnostico()
    if resultado is not None and probabilidad is not None:
        label_tristeza.config(text="Tristeza: "+str(probabilidad[0][3])+"%")
        label_desprecio.config(text="Desprecio: "+str(probabilidad[0][1])+"%")
        label_disgusto.config(text="Disgusto: "+str(probabilidad[0][2])+"%")
        label_felicidad.config(text="Felicidad: "+str(probabilidad[0][0])+"%")
        label_diagnostico.config(text=resultado)
        messagebox.showinfo(message="Este diagnóstico fue dado por una Inteligencia Artificial y puede ser erroneo, por favor visita a un especialista para un diagnóstico más efectivo.",title="Información")
    else:
        label_tristeza.config(text="Tristeza: ")
        label_desprecio.config(text="Desprecio: ")
        label_disgusto.config(text="Disgusto: ")
        label_felicidad.config(text="Felicidad: ")
        label_diagnostico.config(text="")
        messagebox.showerror(message="No se encontraron rostros en la fotografía", title="Error")
        
    
ventana.geometry("1100x700")
#ventana.title("Psycoppy")
ventana.config(bg="#FFC08C")
ventana.resizable(width=False, height=False)
button_subir_imagen = Button(ventana, text="Subir Imagen", command=mostrar_imagen)
button_subir_imagen.place(x=50, y=650)
button_tomar_imagen = Button(ventana, text="Tomar fotografía",command=stop_camara)
button_tomar_imagen.place(x=820, y=650)
#label_titulo = Label(ventana, text="Psycoppy", font=("Arial",28), bg="#FFC08C")
#label_titulo.place(x=50,y=30)
tomar_imagen()
label_la.place(x=50, y=90)

label_resultados = Label(ventana, text="Resultados", font=("Arial",24), bg="#FFC08C")
label_resultados.place(x=800, y=30)

label_tristeza = Label(ventana, text="Tristeza: ", font=("Arial",16), bg="#FFC08C")
label_tristeza.place(x=800, y=110)

label_felicidad = Label(ventana, text="Felicidad: ", font=("Arial",16), bg="#FFC08C")
label_felicidad.place(x=800, y=160)

label_desprecio = Label(ventana, text="Desprecio: ", font=("Arial",16), bg="#FFC08C")
label_desprecio.place(x=800, y=210)

label_disgusto = Label(ventana, text="Disgusto: ", font=("Arial",16), bg="#FFC08C")
label_disgusto.place(x=800, y=260)

label_disgusto = Label(ventana, text="Disgusto: ", font=("Arial",16), bg="#FFC08C")
label_disgusto.place(x=800, y=260)

label_diagnostico = Label(ventana, text="", font=("Arial",16), bg="#FFC08C")
label_diagnostico.place(x=800, y=310)

ventana.mainloop()
   

    
