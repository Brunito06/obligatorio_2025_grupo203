from .Pieza import Pieza

class Requerimiento:
    def __init__(self, maquina, pieza: Pieza, cantidad):
        self.maquina = maquina
        self.pieza = pieza
        self.cantidad = cantidad