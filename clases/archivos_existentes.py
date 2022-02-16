from tkinter import filedialog
class Archivos_Existentes:

    def subeFotografiaExistente():
        archivo = filedialog.askopenfilename(title="Abrir imagen")
        return archivo
