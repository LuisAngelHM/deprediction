from typing import ClassVar
from clases.inteligencia_artificial import Inteligencia_Artificial


class Usuario:
    def __init__(self) -> None:
        fotografia = None

    def setFotografia(self,fotografia):
        self.fotografia = fotografia
    
    def IniciarDiagnostico(self):
        ia = Inteligencia_Artificial()
        rostro = ia.deteccionRostro(self.fotografia)
        if rostro is not None:
            imagen_tratada = ia.tratamientoDeImagen(rostro)
            probabilidad = ia.realizarDiagnostico(imagen_tratada)
            resultado = ia.getDiagnostico()
            return resultado, probabilidad
        return None, None