import datetime
from entities.Pieza import Pieza

class Reposicion:
    def __init__(self, pieza: Pieza, cantidad_lotes: int, fecha_reposicion: datetime):
        self.pieza = pieza
        self.cantidad_lotes = cantidad_lotes
        self.fecha_reposicion = fecha_reposicion

    def costo_reposicion(self):
        return self.cantidad_lotes * self.pieza.lote * self.pieza.costo