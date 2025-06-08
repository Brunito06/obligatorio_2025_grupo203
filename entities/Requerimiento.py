from entities.Pieza import Pieza
from entities.Maquina import Maquina

class Requerimiento:
    def __init__(self, maquina: Maquina, pieza: Pieza, cantidad: int):
        self.maquina = maquina
        self.pieza = pieza
        self.cantidad = cantidad

    def __str__(self):
        return f"Descripcion: {self.pieza.descripcion} - Cantidad: {self.cantidad}"